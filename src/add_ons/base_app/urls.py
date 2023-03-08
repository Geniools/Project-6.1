from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('test/', views.test, name='test'),
	path('transaction/', views.get_transactions, name="transactions"),
	path('transaction/count/', views.get_transactions_count, name='transaction_count'),
	path('transaction/upload/', views.upload_file, name='transaction_upload'),
	path('transaction/<str:transaction_id>/', views.get_transaction, name='transaction'),
	path('transaction/search/<str:keyword>/', views.search_keyword, name='transaction_search_keyword'),
]
