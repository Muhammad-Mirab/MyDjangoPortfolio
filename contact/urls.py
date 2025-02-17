from django.urls import path
from .views import contactView, successView

urlpatterns = [
    path('', contactView, name='contactView'),
    path('success/', successView, name='successView'),
]