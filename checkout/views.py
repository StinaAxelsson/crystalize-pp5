from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from shoppingcart.context import cart_contents


def checkout(request):
    """ View for checkout """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is no products in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kid1fC9IpEuo4QYmRCt5MxuaSYOvoRDBYGMAPPZeJLBLZEubFQvLGeky0PAStFRoq5U4vUnPb2JMjOHIZzRPC6400bsKfZFKL',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
