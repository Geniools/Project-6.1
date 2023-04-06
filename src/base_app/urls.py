from django.urls import path

from base_app.views import upload_file, index

urlpatterns = [
    path("", index, name="base_app_index"),
    path("upload/", upload_file, name="transaction_upload"),
]
