from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_json_api import serializers
from base_app.models import Transaction
import io


class TransactionSerializer(serializers.Serializer):  # Declaring a serializer
    bank_reference = serializers.CharField(max_length=30)
    file_id = serializers.CharField()
    balance_details_id = serializers.CharField()
    category_id = serializers.CharField()
    customer_reference = serializers.CharField(max_length=30)
    entry_date = serializers.DateField()
    guessed_entry_date = serializers.DateField()
    id = serializers.CharField(max_length=4)
    transaction_details = serializers.CharField(max_length=255)
    extra_details = serializers.CharField(max_length=255)
    funds_code = serializers.CharField(max_length=50)

    # Saving instances
    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bank_reference = validated_data.get('bank_reference', instance.bank_reference)
        instance.file_id = validated_data.get('file_id', instance.file_id)
        instance.balance_details_id = validated_data.get('balance_details_id', instance.balance_details_id)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.customer_reference = validated_data.get('customer_reference', instance.customer_reference)
        instance.entry_date = validated_data.get('entry_date', instance.entry_date)
        instance.guessed_entry_date = validated_data.get('guessed_entry_date', instance.guessed_entry_date)
        instance.id = validated_data.get('id', instance.id)
        instance.transaction_details = validated_data.get('transaction_details', instance.transaction_details)
        instance.extra_details = validated_data.get('extra_details', instance.extra_details)
        instance.funds_code = validated_data.get('funds_code', instance.funds_code)
        instance.save()
        return instance


serializer = TransactionSerializer(Transaction)
serializer.data

# I should be able to call serializer.data but has no effect. code below is probably hot garbage

json = JSONRenderer().render(serializer.data)
json

# Deserializing objects
stream = io.BytesIO(json)
data = JSONParser().parse(stream)

serializer = TransactionSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data

transaction = serializer.save()

# .save() will create a new instance.
serializer = TransactionSerializer(data=data)

# .save() will update the existing `transaction` instance.
serializer = TransactionSerializer(transaction, data=data)
