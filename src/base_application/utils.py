import mt940
import json


def parse_mt940_file(file_path) -> dict:
	transaction = mt940.parse(file_path)
	transaction = json.dumps(transaction, indent=4, sort_keys=True, cls=mt940.JSONEncoder)
	transaction = json.loads(transaction)
	return transaction
