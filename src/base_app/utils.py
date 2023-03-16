import json
import mt940

from django.core.files.uploadedfile import UploadedFile

from base_app.models import Transaction, File  # ,BalanceDetails


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
		tr_dict = self._parse()
		
		# BalanceDetails fields
		# balance_details = BalanceDetails()
		
		# File fields
		file = File()
		file.account_identification = tr_dict["account_identification"]
		file.sequence_number = tr_dict["sequence_number"]
		file.statement_number = tr_dict["statement_number"]
		file.transaction_reference_nr = tr_dict["transaction_reference_nr"]
		
		# Transaction fields
		transaction = Transaction()
		tr_bank_reference = tr_dict["bank_reference"]
		tr_customer_reference = tr_dict["customer_reference"]
		tr_entry_date = tr_dict["entry_date"]
		tr_guessed_entry_date = tr_dict["guessed_entry_date"]
		tr_id = tr_dict["id"]
		tr_transaction_details = tr_dict["transaction_details"]
		tr_extra_details = tr_dict["extra_details"]
		tr_funds_code = tr_dict["funds_code"]
	
	# transaction.bank_reference = tr_dict["bank_reference"]
	# transaction.customer_reference = tr_dict["customer_reference"]
	# transaction.entry_date = tr_dict["entry_date"]
	# transaction.guessed_entry_date = tr_dict["guessed_entry_date"]
	# transaction.id = tr_dict["id"]
	# transaction.transaction_details = tr_dict["transaction_details"]
	# transaction.extra_details = tr_dict["extra_details"]
	# transaction.funds_code = tr_dict["funds_code"]
	
	def save_to_nosql_db(self, database_collection) -> dict:
		transaction = {"content": self.file.read().decode("utf-8")}
		database_collection.insert_one(transaction)
		return transaction

# Transaction fields
