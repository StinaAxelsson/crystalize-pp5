from django.db import models
from products.models import Product
from profiles.models import UserProfile


class WishList(models.Model):
    """
    Model for saved items in a wishlist
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    logged_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'WishList ({self.logged_user})'
