from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from shoppingcart.context import cart_contents

import stripe


def checkout(request):
    """ View for checkout """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is no products in your cart at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kid1fC9IpEuo4QYmRCt5MxuaSYOvoRDBYGMAPPZeJLBLZEubFQvLGeky0PAStFRoq5U4vUnPb2JMjOHIZzRPC6400bsKfZFKL',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
