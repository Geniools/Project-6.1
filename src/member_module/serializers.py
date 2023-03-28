from rest_framework import serializers

from member_module.models import Member, LinkedTransaction


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email']


class LinkedTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkedTransaction
        fields = ['id', 'member_id', 'transaction_bank_reference']
