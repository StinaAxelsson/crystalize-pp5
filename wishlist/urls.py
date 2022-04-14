from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('save/<int:product_id>/', views.save_to_wishlist, name='save_to_wishlist'),
    path('delete/<int:product_id>/', views.delete_in_wishlist, name='delete_in_wishlist'),
]
