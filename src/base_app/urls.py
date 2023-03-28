from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from . import views
from .models import Transaction
from member_module.models import Member

router = routers.DefaultRouter()
router.register(r'transaction', views.TransactionViewSet)
router.register(r'file', views.FileViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'BalanceDetails', views.BalanceDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
    # path('transaction/', views.get_transactions, name="transactions"),
    # path('transaction/count/', views.get_transactions_count, name='transaction_count'),
    # path('transaction/upload/', views.upload_file, name='transaction_upload'),
    # path('transaction/<str:transaction_id>/', views.get_transaction, name='transaction'),
    # path('transaction/search/<str:keyword>/', views.search_keyword, name='transaction_search_keyword'),
    path('schema',
         get_schema_view(title="Transaction API", description="API for transactions", version="1.0.0", patterns=list(Member.objects.all())),
         name='openapi-schema')
]
