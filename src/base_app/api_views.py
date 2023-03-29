from rest_framework import viewsets, permissions

from base_app.serializers import TransactionSerializer, FileSerializer, CategorySerializer, CurrencySerializer, BalanceDetailsSerializer
from base_app.models import Transaction, File, Category, Currency, BalanceDetails


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows transactions to be viewed or edited.
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows files (mt940 files) to be viewed or edited.
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows categories to be viewed or edited.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows currencies to be viewed or edited.
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]


class BalanceDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    # API endpoint that allows balance details to be viewed or edited.
    queryset = BalanceDetails.objects.all()
    serializer_class = BalanceDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
