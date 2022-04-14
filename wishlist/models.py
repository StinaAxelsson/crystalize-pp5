from django.db import models
from products.models import Product


class WishList(models.Model):
    """
    Model for saved items in a wishlist
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
