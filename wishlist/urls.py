from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('save/<int:product_id>/', views.save_to_wishlist, name='save_to_wishlist'),
]
