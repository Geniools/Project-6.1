from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Member

# Create your views here.


def jsonTest(request):
    data = list(Member.objects.values())
    return JsonResponse(data, safe=False)