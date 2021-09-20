from django.urls import path

from .views import BrandListView, BrandCreateView

urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
    path('brands/create/', BrandCreateView.as_view(), name='brands_create'),
]
