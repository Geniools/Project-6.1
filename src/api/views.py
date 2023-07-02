from rest_framework import viewsets, permissions, mixins

from api.permissions import IsTreasurerIsSuperuserOrReadOnly
from api.serializers import *


# ViewSets templates
class CreateAndListOnlyViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class UpdateAndListOnlyViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


# Base app
class TransactionViewSet(UpdateAndListOnlyViewSet):
    # API endpoint that allows transactions to be viewed or updated.
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows files (mt940 files) to be viewed
    queryset = File.objects.all().order_by('-registration_time')
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class CategoryViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows categories to be viewed or created.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class CurrencyViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows currencies to be viewed or created.
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class BalanceDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows balance details to be viewed.
    queryset = BalanceDetails.objects.all()
    serializer_class = BalanceDetailsSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


# Cash module
class CashTransactionViewSet(CreateAndListOnlyViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = CashTransaction.objects.all()
    serializer_class = CashTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


# Member module
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class LinkedTransactionViewSet(CreateAndListOnlyViewSet):
    queryset = LinkedTransaction.objects.all()
    serializer_class = LinkedTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]
