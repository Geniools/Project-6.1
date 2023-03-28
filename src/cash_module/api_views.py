from rest_framework import viewsets, permissions

from cash_module.models import CashTransaction
from cash_module.serializers import CashTransactionSerializer


class CashTransactionViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = CashTransaction.objects.all()
    serializer_class = CashTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
