from rest_framework import serializers

from base_app.models import Transaction, File, Category, Currency, BalanceDetails


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
