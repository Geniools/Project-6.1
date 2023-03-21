from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Member, LinkedTransaction

# Create your views here.


#JSON Test is made with the intention of getting the entries from the db as JSON format
def jsonTest(request):
    data = list(LinkedTransaction.objects.values())
    return JsonResponse(data, safe=False)