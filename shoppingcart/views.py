from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ View shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product and quantity of it in the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Successfully added {product.name} to your shoppingcart!')

    request.session['cart'] = cart

    return redirect(redirect_url)


def change_cart(request, item_id):
    """ Change quantity in cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop[item_id]
        messages.success(request, f'Deleted {product.name} from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def delete_in_cart(request, item_id):
    """ Change quantity in cart"""
    product = get_object_or_404(Product, pk=item_id)

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Deleted {product.name} from your cart')

        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error! Remove item {e} from cart ')
        return HttpResponse(status=500)

