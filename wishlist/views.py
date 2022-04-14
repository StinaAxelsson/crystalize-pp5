from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from products.models import Product
from wishlist.models import WishList


def wishlist(request):
    """Show wishlist"""

    template = 'wishlist/wishlist.html'
    wishlist = WishList.objects.all()

    context = {
        'wishlist': wishlist,
    }
    return render(request, template, context)


def save_to_wishlist(request, product_id):
    """ Save a product to a wishlist """

    product = get_object_or_404(Product, pk=product_id)

    WishList.objects.create(
        product=product
    )

    messages.success(request, f'{product.name} has successfully saved to your wishlist')

    return redirect(reverse('product_detail', args=[product.id]))
