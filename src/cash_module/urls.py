from django.urls import path
from cash_module.views import jsonTest

urlpatterns = [
    path("test/", jsonTest, name="test"),
]
