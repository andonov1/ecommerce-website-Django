from django.urls import path, include

from ecommerce.products.views import product_list_view, AddProductView, product_detail_view

urlpatterns = [
    path('', product_list_view, name='products list'),
    path('add/', AddProductView.as_view(), name='add product'),
    path('<int:pk>/', product_detail_view, name='product detail'),
]
