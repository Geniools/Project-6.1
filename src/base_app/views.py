import json

from bson import json_util
from bson.objectid import ObjectId

from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages

from base_app.forms import UploadMT940Form
from base_app.utils import MT940DBParser
from . import transactions_collection
from .models import Transaction, File, Category, Currency, BalanceDetails

#JSON Test is made with the intention of getting the entries from the db as JSON format
def jsonTest(request):
    data = list(BalanceDetails.objects.values())
    return JsonResponse(data, safe=False)

def index(request):
    answer = {
        "message": "SportsAccounting API",
        "api":     {
            "Retrieve all transactions":                            "/api/transaction/",
            "Get the total number of transactions in the NoSQL DB": "/api/transaction/count",
            "Upload a file":                                        "/api/transaction/upload",
            "Retrieve a specific transaction":                      "/api/transaction/<transaction_id>",
            "Search for a keyword":                                 "/api/transaction/search/<keyword>"
        }
    }
    return JsonResponse(answer)


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
        # Feed the form with the POST data
        form = UploadMT940Form(request.POST, request.FILES)
        if form.is_valid():
            # Get all the files from the form
            files = request.FILES.getlist("file")
            for file in files:
                # Checking if the file is not too big (more than 2.5 MB)
                if not file.multiple_chunks():
                    handler = MT940DBParser(file)
                    # handler.save_to_nosql_db(transactions_collection)
                    handler.save_to_sql_db()
                    # Add a success message
                    messages.success(request, f"File \"{file.name}\" uploaded successfully.")
                else:
                    # Add an error message if the file is too big
                    messages.error(request, "The file is too big.")
    else:
        # If GET method or any other method called, return an empty form
        form = UploadMT940Form()

    return render(request, "base_app/upload_transaction.html", {"form": form})
