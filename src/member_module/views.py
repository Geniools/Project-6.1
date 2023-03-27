from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Member, LinkedTransaction


# Create your views here.

class MemberSerializer(serializers.Serializer):
    # Member model
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=60)


class LinkedTransactionSerializer(serializers.Serializer):
    # Linked Transactions model
    id = serializers.IntegerField()
    member_id = serializers.IntegerField()
    transaction_bank_reference = serializers.CharField(max_length=30)


# JSON Test is made with the intention of getting the entries from the db as JSON format
def jsonTest(request):
    dataMember = Member.objects.values()
    dataLinkedTransaction = LinkedTransaction.objects.values()

    # return JsonResponse(data, safe=False)

    serializerMember = MemberSerializer(dataMember)
    serializeLinkedTransaction = LinkedTransactionSerializer(dataLinkedTransaction)

    return serializerMember;
