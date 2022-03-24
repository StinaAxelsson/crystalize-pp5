from django.shortcuts import render


def view_cart(request):
    """ View shopping cart """
    return render(request, 'cart/cart.html')
