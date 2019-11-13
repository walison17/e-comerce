from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<str:slug>', category, name='category'),
    path('produtos/<str:slug>', product, name='product'),
]