from django.urls import path, include
from .views import CategoryViewSet, DetialView

urlpatterns = [
    path('categories/', CategoryViewSet.as_view(), name='category'),
    path('categories/<int:pk>/', DetialView.as_view(), name='category_detail'),
]
