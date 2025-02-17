from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminView, name="adminView"),
]