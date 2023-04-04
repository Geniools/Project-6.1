from rest_framework import serializers
from rest_framework.exceptions import NotFound

from cash_module.models import CashTransaction
from base_app.models import Currency, BalanceDetails


class CashTransactionSerializer(serializers.HyperlinkedModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=5, required=True)
    currency = serializers.ChoiceField(choices=[currency.name for currency in Currency.objects.all()], required=True)
    
    class Meta:
        model = CashTransaction
        fields = ['id', 'source', 'target', 'amount', 'currency']
    
    def create(self, validated_data):
        balance_details = BalanceDetails()
        balance_details.amount = validated_data['amount']
        try:
            balance_details.currency_type_id = Currency.objects.get(name=validated_data['currency'])
        except Currency.DoesNotExist:
            raise NotFound(detail='Currency not found')
        balance_details.save()
        return CashTransaction.objects.create(source=validated_data['source'], target=validated_data['target'], balance_details_id=balance_details)
    
    def update(self, instance, validated_data):
        instance.source = validated_data.get('source', instance.source)
        instance.target = validated_data.get('target', instance.target)
        instance.balance_details_id.amount = validated_data.get('amount', instance.balance_details_id.amount)
        try:
            instance.balance_details_id.currency_type_id = Currency.objects.get(name=validated_data['currency'])
        except Currency.DoesNotExist:
            raise NotFound(detail='Currency not found')
        instance.balance_details_id.save()
        instance.save()
        return instance
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'source': instance.source,
            'target': instance.target,
            'amount': instance.balance_details_id.amount,
            'currency': instance.balance_details_id.currency_type_id.name
        }
