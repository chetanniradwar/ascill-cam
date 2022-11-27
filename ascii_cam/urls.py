from http.client import HTTPResponse
from django.urls import path
from . import views
urlpatterns = [
    path("", views.videoCam)
]
