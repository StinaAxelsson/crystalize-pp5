from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('change/<item_id>/', views.change_cart, name='change_cart'),
    path('delete/<item_id>/', views.delete_in_cart, name='delete_in_cart'),
]