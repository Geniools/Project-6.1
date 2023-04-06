from rest_framework import permissions

from main.permissions import IsTreasurerIsSuperuserOrReadOnly
from cash_module.models import CashTransaction
from cash_module.serializers import CashTransactionSerializer
from base_app.api_views import CreateAndListOnlyViewSet


class CashTransactionViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = CashTransaction.objects.all()
    serializer_class = CashTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]
