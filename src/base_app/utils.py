import json
import mt940

from django.core.files.uploadedfile import UploadedFile

from base_app.models import Transaction, File, BalanceDetails, Currency


class MT940DBParser:
    def __init__(self, file: UploadedFile):
        self.__file = file

    @property
    def file(self) -> UploadedFile:
        return self.__file

    def _parse(self) -> dict:
        transaction = mt940.parse(self.file)
        transaction = json.dumps(transaction, indent=4, sort_keys=True, cls=mt940.JSONEncoder)
        transaction = json.loads(transaction)
        return transaction

    def save_to_sql_db(self):
        """
        This method will save the parsed MT940 file to the SQL database.
        :return: None
        """
        file_content = self._parse()

        # File fields -> saving each of the balance details to the File model
        file = File()
        file.available_balance_id = self._get_balance_details(file_content["available_balance"])
        file.final_closing_balance_id = self._get_balance_details(file_content["final_closing_balance"])
        file.final_opening_balance_id = self._get_balance_details(file_content["final_opening_balance"])
        file.forward_available_balance_id = self._get_balance_details(file_content["forward_available_balance"])
        file.account_identification = file_content["account_identification"]
        file.sequence_number = file_content["sequence_number"]
        file.statement_number = file_content["statement_number"]
        file.transaction_reference_nr = file_content["transaction_reference"]

        # Saving the file
        file.save()

        # Saving the transactions
        for transaction in file_content["transactions"]:
            tr = Transaction()
            tr.file_id = file
            tr.bank_reference = transaction["bank_reference"]
            tr.customer_reference = transaction["customer_reference"]
            tr.entry_date = transaction["entry_date"]
            tr.guessed_entry_date = transaction["guessed_entry_date"]
            tr.id = transaction["id"]
            tr.transaction_details = transaction["transaction_details"]
            tr.extra_details = transaction["extra_details"]
            tr.funds_code = transaction["funds_code"]
            tr.balance_details_id = self._get_balance_details(transaction)
            tr.save()

    def __get_currency(self, currency_type: str) -> Currency:
        """
        This method will return the currency object from the database.
        :param currency_type: The currency type as a three-letter code in ISO 4217.
        :return: The currency object.
        """
        try:
            return Currency.objects.get(name__contains=currency_type.upper())
        except Currency.DoesNotExist:
            return Currency.objects.create(name=currency_type)

    def _get_balance_details(self, details: dict) -> BalanceDetails:
        """
        This method will return an instance of  BalanceDetails.
        :param details: The balance details in a dictionary format.
        :return: The balance details object.
        """
        amount = details["amount"]["amount"]
        currency_type = self.__get_currency(details["amount"]["currency"])
        date = details["date"]
        status = details["status"]
        return BalanceDetails.objects.create(amount=amount, currency_type_id=currency_type, date=date, status=status)

    def save_to_nosql_db(self, database_collection) -> dict:
        """
        This method will save the parsed MT940 file to the NoSQL database.
        :param database_collection: The collection in which the file will be saved.
        :return: The saved transaction in a dictionary format.
        """
        transaction = {"content": self.file.read().decode("utf-8")}
        database_collection.insert_one(transaction)
        return transaction
