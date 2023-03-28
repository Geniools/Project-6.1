from django.urls import path
from member_module.views import jsonTest

urlpatterns = [
    path("test/", jsonTest, name="test"),
]
