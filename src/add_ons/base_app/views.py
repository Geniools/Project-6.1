import json

from bson import json_util
from bson.objectid import ObjectId
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from . import transactions_collection
from .forms import UploadMT940Form
from .utils import parse_mt940_file


def index(request):
	answer = {
		"message": "Welcome to the SportsAccounting API",
		"api":     {
			"test":                  "/api/test",
			"getTransactionsAmount": "/api/getTransactionsCount",
			"getTransactions":       "/api/getTransactions",
			"getTransaction":        "/api/getTransaction/<transaction_id>",
			"searchKeyword":         "/api/searchKeyword/<keyword>",
			"uploadMT940File":       "/api/uploadFile"
		}
	}
	return JsonResponse(answer)


def test(request):
	# Change the path to the file you want to test
	# file_path = "D:\\Programming\\Python\\Project-6.1\\test_mt940_files\\test1.txt"
	# transaction = parse_mt940_file(file_path)
	# transactions_collection.insert_one(transaction)
	return HttpResponse("I have to write a test here.")


def get_transactions_count(request):
	response = {
		"transactionsCount": transactions_collection.count_documents({})
	}
	return JsonResponse(response)


def get_transactions(request):
	all_transactions = []
	
	for transaction in transactions_collection.find():
		# print(transaction)
		all_transactions.append(transaction)
	
	return JsonResponse(json.loads(json_util.dumps(all_transactions)), safe=False)


def get_transaction(request, transaction_id: str):
	transaction = transactions_collection.find_one({"_id": ObjectId(transaction_id)})
	
	if not transaction:
		return Http404("Transaction not found")
	
	return JsonResponse(json.loads(json_util.dumps(transaction)))


def search_keyword(request, keyword: str):
	# TODO: implement functionality to search for keyword within transactions
	return HttpResponse(f"The keyword that this app must search for is: <b>{keyword}</b>")


def upload_file(request):
	if request.POST:
		form = UploadMT940Form(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES["file"]
			transaction = parse_mt940_file(file)
			# Save the transaction to the database
			transactions_collection.insert_one(transaction)
			return JsonResponse(json.loads(json_util.dumps(transaction)))
	else:
		# If GET method or any other method called, return an empty form
		form = UploadMT940Form()
	
	return render(request, "base_app/upload_transaction.html", {"form": form})
