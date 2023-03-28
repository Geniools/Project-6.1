import json

from bson import json_util
from bson.objectid import ObjectId

from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib import messages
from rest_framework import viewsets, permissions
from base_app.forms import UploadMT940Form
from base_app.utils import MT940DBParser
from . import transactions_collection
from .models import Transaction, File, Category, Currency, BalanceDetails
from .serializers import TransactionSerializer, FileSerializer, CategorySerializer, CurrencySerializer, BalanceDetailsSerializer


def index(request):
    answer = {
        "message": "SportsAccounting API",
        "api": {
            "Retrieve all transactions": "/api/transaction/",
            "Get the total number of transactions in the NoSQL DB": "/api/transaction/count",
            "Upload a file": "/api/transaction/upload",
            "Retrieve a specific transaction": "/api/transaction/<transaction_id>",
            "Search for a keyword": "/api/transaction/search/<keyword>"
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


@login_required
def upload_file(request):
    # Check if the user is a treasurer or a superuser
    if not request.user.is_treasurer and not request.user.is_superuser:
        raise PermissionDenied("You are not authorized to view this page.")

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
                    handler.save_to_nosql_db(transactions_collection)
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


class TransactionViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrencyViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]


class BalanceDetailsViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = BalanceDetails.objects.all()
    serializer_class = BalanceDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
