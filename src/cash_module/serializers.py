from rest_framework import serializers

from cash_module.models import CashTransaction


class CashTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CashTransaction
        fields = ['id', 'balance_details_id', 'source', 'target']
