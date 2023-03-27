from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import CashTransaction
from .schemas import CashTSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Create your views here.

#JSON Test is made with the intention of getting the entries from the db as JSON format
def jsonTest(request):
    return 0;
    #code here