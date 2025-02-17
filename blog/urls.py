from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogView, name="blogView"),
    path('category/<str:category>/', views.blogCategorizedView, name='categorized_blog'),
    path("<str:pk>/", views.blogDetail, name="blogDetail"),
]