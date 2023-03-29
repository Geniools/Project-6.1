import json
import mt940

from typing import Optional
from functools import cached_property

from django.core.files.uploadedfile import UploadedFile

from base_app.models import Transaction, File, BalanceDetails, Currency
from . import transactions_collection


class MT940DBParser:
    def __init__(self, file: UploadedFile):
        self.__file = file
        # A list to keep track of all saved objects in the database (can be used for deleting them if an error happens)
        self._created_db_objects = []
        # The id of the inserted query in the no sql database (can be used to access/delete the nosql DB in case of an error)
        self._no_sql_id = None
    
    @property
    def file(self) -> UploadedFile:
        return self.__file
    
    @cached_property
    def file_content(self) -> str:
        return self.file.read().decode("utf-8")
    
    def _parse(self) -> dict:
        """
        This method will parse the MT940 file and return the parsed content.
        :return: The parsed content.
        """
        transaction = mt940.parse(self.file_content)
        transaction = json.dumps(transaction, indent=4, sort_keys=True, cls=mt940.JSONEncoder)
        transaction = json.loads(transaction)
        # import pprint
        # pprint.pprint(transaction)
        return transaction
    
    def save_to_sql_db(self) -> File:
        """
        This method will save the parsed MT940 file to the SQL database.
        :return: None
        """
        file = File()
        try:
            file_content = self._parse()
            # File fields -> saving each of the balance details to the File model
            file.available_balance_id = self._get_balance_details(file_content.get("available_balance"))
            file.final_closing_balance_id = self._get_balance_details(file_content.get("final_closing_balance"))
            file.final_opening_balance_id = self._get_balance_details(file_content.get("final_opening_balance"))
            file.forward_available_balance_id = self._get_balance_details(file_content.get("forward_available_balance"))
            file.transaction_reference_nr = file_content.get("transaction_reference")
            file.related_reference_nr = file_content.get("related_reference")
            file.account_identification = file_content.get("account_identification")
            file.statement_number = file_content.get("statement_number")
            file.sequence_number = file_content.get("sequence_number")
            # Saving the file
            file.save()
            self._created_db_objects.append(file)
            
            # Saving the transactions
            for transaction in file_content.get("transactions"):
                tr = Transaction()
                tr.bank_reference = transaction.get("bank_reference")
                tr.file_id = file
                tr.balance_details_id = self._get_balance_details(transaction)
                tr.customer_reference = transaction.get("customer_reference")
                tr.entry_date = transaction.get("entry_date")
                tr.guessed_entry_date = transaction.get("guessed_entry_date")
                tr.transaction_identification_code = transaction.get("id")
                tr.transaction_details = transaction.get("transaction_details")
                tr.extra_details = transaction.get("extra_details")
                tr.funds_code = transaction.get("funds_code")
                tr.save()
                self._created_db_objects.append(tr)
            
            return file
        except Exception as ex:
            # Delete any objects that were created before the exception occurred
            self.__delete_created_db_objects()
            raise ex
    
    def __get_currency(self, currency_type: str) -> Optional[Currency]:
        """
        This method will return the currency object from the database.
        :param currency_type: The currency type as a three-letter code in ISO 4217.
        :return: The currency object or None.
        """
        if currency_type is None:
            return
        
        try:
            currency = Currency.objects.get(name__contains=currency_type.upper())
        except Currency.DoesNotExist:
            currency = Currency.objects.create(name=currency_type)
        
        self._created_db_objects.append(currency)
        return currency
    
    def _get_balance_details(self, details: dict) -> Optional[BalanceDetails]:
        """
        This method will return an instance of  BalanceDetails.
        :param details: The balance details in a dictionary format.
        :return: The balance details object or None.
        """
        if details is None:
            return
        
        amount = details["amount"]["amount"]
        currency_type = self.__get_currency(details["amount"]["currency"])
        date = details["date"]
        status = details["status"]
        balance_details = BalanceDetails.objects.create(amount=amount, currency_type_id=currency_type, date=date, status=status)
        
        self._created_db_objects.append(balance_details)
        return balance_details
    
    def __delete_created_db_objects(self):
        for obj in self._created_db_objects:
            obj.delete()
    
    def save_to_nosql_db(self) -> dict:
        """
        This method will save the parsed MT940 file to the NoSQL database.
        :return: The saved transaction in a dictionary format.
        """
        transaction = {"content": self.file_content}
        # Inserting the contents of the file in the NoSQL DB and saving its id for future use
        self._no_sql_id = transactions_collection.insert_one(transaction).inserted_id
        return transaction
