from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ View all products, with sorting nd search"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
