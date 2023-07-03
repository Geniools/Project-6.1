from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list-json/', views.list_from_api_json, name='list-json'),
    path('list-json/<int:page>/', views.list_from_api_json, name='list-json'),
    path('list-xml/', views.list_from_api_xml, name='list-xml'),
    path('list-xml/<int:page>/', views.list_from_api_xml, name='list-xml'),
]
