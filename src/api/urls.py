from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views

router = routers.DefaultRouter()
router.register(r'file', views.FileViewSet)
router.register(r'transaction', views.TransactionViewSet)
router.register(r'transaction-category', views.CategoryViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'balance-details', views.BalanceDetailsViewSet)
router.register(r'cash-transaction', views.CashTransactionViewSet)
router.register(r'member', views.MemberViewSet)
router.register(r'linked-member-transaction', views.LinkedTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'schema/', get_schema_view(
            title="Sports Accounting API",
            description="API for the sports accounting application for retrieving data",
            version="1.0.0",
        ), name='openapi-schema'
    ),
]
