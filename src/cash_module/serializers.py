from rest_framework import serializers
from .models import CashTransaction


class CashTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTransaction
        fields = ['id', 'balance_details_id', 'source', 'target']