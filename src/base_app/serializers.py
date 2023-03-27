from rest_framework import serializers
from .models import Transaction, File, Category, Currency, BalanceDetails


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['bank_reference', 'file_id', 'balance_details_id', 'category_id', 'customer_reference', 'entry_date',
                  'guessed_entry_date', 'id', 'transaction_details', 'extra_details', 'funds_code']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'available_balance_id', 'final_closing_balance_id', 'final_opening_balance_id',
                  'forward_available_balance_id', 'account_identification',
                  'sequence_number', 'statement_number', 'transaction_reference_nr']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name']


class BalanceDSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceDetails
        fields = ['id', 'amount', 'currency_type_id', 'date', 'status']