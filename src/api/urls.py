from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views
from api import schema_views

router = routers.DefaultRouter()
# Base app
router.register(r'file', views.FileViewSet)
router.register(r'transaction', views.TransactionViewSet)
router.register(r'transaction-category', views.CategoryViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'balance-details', views.BalanceDetailsViewSet)
# Cash module
router.register(r'cash-transaction', views.CashTransactionViewSet)
# Member module
router.register(r'member', views.MemberViewSet)
router.register(r'linked-member-transaction', views.LinkedTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('member-schema-validator/', schema_views.MemberSchemaValidatorView.as_view(), name='member-schema-validator'),
    path('balance-details-schema-validator/', schema_views.BalanceDetailsSchemaValidator.as_view(), name='balance-details-schema-validator'),
    path('cash-schema-validator/', schema_views.CashSchemaValidator.as_view(), name='cash-schema-validator'),
    path('category-schema-validator/', schema_views.CategorySchemaValidator.as_view(), name='category-schema-validator'),
    path('currency-schema-validator/', schema_views.CurrencySchemaValidator.as_view(), name='currency-schema-validator'),
    path('file-schema-validator/', schema_views.FileSchemaValidator.as_view(), name='file-schema-validator'),
    path('transaction-schema-validator/', schema_views.TransactionSchemaValidator.as_view(), name='transaction-schema-validator'),
    path(
        'schema/', get_schema_view(
            title="Sports Accounting API",
            description="API for the sports accounting application for retrieving data",
            version="1.0.0",
        ), name='openapi-schema'
    ),
]
