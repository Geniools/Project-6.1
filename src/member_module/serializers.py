from rest_framework import serializers
from .models import Member, LinkedTransaction


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email']


class LinkedTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedTransaction
        fields = ['id', 'member_id', 'transaction_bank_reference']
