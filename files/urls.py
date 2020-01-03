from django.urls import path

from . import views

app_name = "files"

urlpatterns = [
    path("", views.FileView.as_view(), name="list"),
    # path("upload/", views.FileUploadCreateView.as_view(), name="upload"),
]
