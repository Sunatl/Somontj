from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('inquiries/', inquiry_list, name='inquiry-list'),
    path('inquiries/<int:pk>/', inquiry_detail, name='inquiry-detail'),
] 

