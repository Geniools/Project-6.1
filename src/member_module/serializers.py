from rest_framework import serializers

from member_module.models import Member, LinkedTransaction


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
