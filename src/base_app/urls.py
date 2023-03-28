from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from base_app import api_views as views

router = routers.DefaultRouter()
router.register(r'transaction', views.TransactionViewSet)
router.register(r'file', views.FileViewSet)
router.register(r'transaction-category', views.CategoryViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'balance-details', views.BalanceDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path(
    #     'schema',
    #     get_schema_view(title="Transaction API", description="API for transactions", version="1.0.0", patterns=list(Member.objects.all())),
    #     name='openapi-schema'
    # )
]
