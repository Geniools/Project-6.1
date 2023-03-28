from django.urls import path, include
from rest_framework import routers

from cash_module import api_views as views

router = routers.DefaultRouter()
router.register(r'cash-transaction', views.CashTransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
