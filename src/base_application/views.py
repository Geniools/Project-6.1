from src.base_application import app
from src.base_application import transactions_collection
from utils import parse_mt940_file

from flask import jsonify, request, make_response
from bson import json_util
from bson.objectid import ObjectId

import json


# Views (API)

# Test function with an existing MT940 file
@app.route("/")
def index():
	answer = {
		"message": "Welcome to the SportsAccounting API",
		"api":     {
			"test":                  "/api/test",
			"getTransactionsAmount": "/api/getTransactionsCount",
			"getTransactions":       "/api/getTransactions",
			"getTransaction":        "/api/getTransaction/<transaction_id>",
			"uploadMT940File":       "/api/uploadMT940File"
		}
	}
	return make_response(jsonify(answer), 200)


@app.route("/api/test")
def test():
	# Change the path to the file you want to test
	file_path = "D:\\Programming\\Python\\Project-6.1\\test_mt940_files\\test1.txt"
	transaction = parse_mt940_file(file_path)
	transactions_collection.insert_one(transaction)
	return make_response(json.loads(json_util.dumps(transaction)), 200)


@app.route("/api/getTransactionsCount", methods=["GET"])
def get_transactions_count():
	response = {
		"transactionsCount": transactions_collection.count_documents({})
	}
	return response


@app.route("/api/getTransactions", methods=["GET"])
def get_transactions():
	all_transactions = []
	
	for transaction in transactions_collection.find():
		print(transaction)
		all_transactions.append(transaction)
	
	return make_response(json.loads(json_util.dumps(all_transactions)), 200)


@app.route("/api/getTransaction/<transaction_id>", methods=["GET"])
def get_transaction(transaction_id):
	transaction = transactions_collection.find_one({"_id": ObjectId(transaction_id)})
	
	if not transaction:
		return make_response(jsonify(error="Transaction not found"), 404)
	
	return make_response(json.loads(json_util.dumps(transaction)), 200)


@app.route("/api/uploadMT940File", methods=["POST"])
def upload_file():
	if "file" not in request.files:
		return make_response(jsonify(error="No file part"), 400)
	
	file = request.files["file"]
	# TODO: Test and parse the file
	transaction = parse_mt940_file(file)
	# Save the transaction to the database
	transactions_collection.insert_one(transaction)
	
	return make_response(json.loads(json_util.dumps(transaction)), 200)


@app.errorhandler(404)
def not_found(e):
	return make_response(jsonify(error=str(e)), 404)
