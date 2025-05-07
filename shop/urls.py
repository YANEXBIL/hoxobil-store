# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch-printify-products/', views.fetch_printify_products, name='fetch_printify_products'),
    path('create-printify-product/', views.create_printify_product_view, name='create_printify_product'),
]
