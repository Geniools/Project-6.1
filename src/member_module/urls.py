from django.urls import path, include
from rest_framework import routers

from member_module import api_views as views

router = routers.DefaultRouter()
router.register(r'member', views.MemberViewSet)
router.register(r'linked-member-transaction', views.LinkedTransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
