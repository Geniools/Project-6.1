from django.urls import path

from . import views
from rest_framework.schemas import get_schema_view
from .views import TransactionSerializer
from .models import Transaction, File

serializer_class = TransactionSerializer

urlpatterns = [
	path('', views.index, name='index'),
	path('transaction/', views.get_transactions, name="transactions"),
	path('transaction/count/', views.get_transactions_count, name='transaction_count'),
	path('transaction/upload/', views.upload_file, name='transaction_upload'),
	path('transaction/<str:transaction_id>/', views.get_transaction, name='transaction'),
	path('transaction/search/<str:keyword>/', views.search_keyword, name='transaction_search_keyword'),
	#path("test/", jsonTest, name="test"),
	path('schema', get_schema_view(
		title="Transaction API",
		description="API for transactions",
		version="1.0.0",
		patterns= Transaction.objects.filter()
	), name='openapi-schema'),

]
