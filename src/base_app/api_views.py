from rest_framework import viewsets, permissions, mixins

from main.permissions import IsTreasurerIsSuperuserOrReadOnly
from base_app.serializers import TransactionSerializer, FileSerializer, CategorySerializer, CurrencySerializer, BalanceDetailsSerializer
from base_app.models import Transaction, File, Category, Currency, BalanceDetails


class CreateAndListOnlyViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class UpdateAndListOnlyViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class TransactionViewSet(UpdateAndListOnlyViewSet):
    # API endpoint that allows transactions to be viewed or updated.
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreasurerIsSuperuserOrReadOnly]


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows files (mt940 files) to be viewed
    queryset = File.objects.all()
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
