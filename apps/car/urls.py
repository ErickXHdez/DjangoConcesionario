from django.urls import path

from .views import BrandListView, BrandCreateView, BrandRetrieveView, BrandUpdateView, BrandDestroyView

urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
    path('brands/create/', BrandCreateView.as_view(), name='brands_create'),
    path('brands/<int:id>/', BrandRetrieveView.as_view(), name='brands_retrieve'),
    path('brands/<int:id>/update/', BrandUpdateView.as_view(), name='brands_update'),
    path('brands/<int:id>/delete/', BrandDestroyView.as_view(), name='brands_delete'),

]
