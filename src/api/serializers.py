from rest_framework import serializers
from rest_framework.exceptions import NotFound

from base_app.models import Transaction, File, Category, Currency, BalanceDetails
from cash_module.models import CashTransaction
from member_module.models import Member, LinkedTransaction


# Base app serializers
class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = [
            'id', 'available_balance_id', 'final_closing_balance_id', 'final_opening_balance_id', 'forward_available_balance_id', 'transaction_reference_nr',
            'related_reference_nr', 'account_identification', 'statement_number', 'sequence_number', 'registration_time'
        ]
        read_only_fields = ['__all__']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id', 'bank_reference', 'file_id', 'balance_details_id', 'category_id', 'custom_description', 'customer_reference', 'entry_date', 'guessed_entry_date',
            'transaction_identification_code', 'transaction_details', 'extra_details', 'funds_code'
        ]
        read_only_fields = [
            'id', 'bank_reference', 'file_id', 'balance_details_id', 'customer_reference', 'entry_date', 'guessed_entry_date',
            'transaction_identification_code', 'transaction_details', 'extra_details', 'funds_code'
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        read_only_fields = ['__all__']


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['name']
        read_only_fields = ['__all__']


class BalanceDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BalanceDetails
        fields = ['amount', 'currency_type_id', 'date', 'status']
        read_only_fields = ['__all__']


# Cash module serializers
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


# Member module serializers
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email']
    
    def update(self, instance, validated_data):
        validated_data.pop('first_name', None)  # Prevents changing first name
        validated_data.pop('last_name', None)  # Prevents changing last name
        return super().update(instance, validated_data)


class LinkedTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkedTransaction
        fields = ['id', 'member_id', 'transaction_bank_reference']
        read_only_fields = ['__all__']
