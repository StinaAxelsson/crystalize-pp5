from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from wishlist.models import WishList
from profiles.models import UserProfile


@login_required
def wishlist(request):
    """Show wishlist"""
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishList.objects.filter(logged_user=user)

    context = {
        'wishlist': wishlist,
    }
    template = 'wishlist/wishlist.html'
    return render(request, template, context)


@login_required
def save_to_wishlist(request, product_id):
    """ Save a product to a wishlist """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    WishList.objects.create(
        product=product,
        logged_user=user,
    )

    messages.success(request, f'{product.name} has successfully saved to your wishlist')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_in_wishlist(request, product_id):
    """ Delete a product from wishlist """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    WishList.objects.filter(product=product, logged_user=user).delete()

    return redirect(reverse('product_detail', args=[product.id]))
