from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Avg

from reviews.models import Review
from reviews.forms import ReviewForm
from .models import Product, Category
from .forms import ProductForm
from profiles.models import UserProfile
from wishlist.models import WishList


def all_products(request):
    """ View all products, with sorting nd search"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critera!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    wishlist = None
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = WishList.objects.filter(logged_user=user)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'wishlist': wishlist,

    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to products details"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    reviews_by_user = None

    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating is not None:
        avg_rating = round(avg_rating * 2) / 2

    if not request.user.is_authenticated:
        context = {
            'product': product,
            'reviews': reviews,
            'avg_rating': avg_rating,
        }
        return render(request, 'products/product_detail.html', context)
    else:
        user = get_object_or_404(UserProfile, user=request.user)
        reviews_by_user = Review.objects.filter(
            product=product,
            user=get_object_or_404(UserProfile, user=request.user)
        )
        wishlist = WishList.objects.filter(
                   logged_user=user, product=product_id)

        form = ReviewForm()

        context = {
            'product': product,
            'reviews': reviews,
            'form': form,
            'reviews_by_user': reviews_by_user,
            'avg_rating': avg_rating,
            'wishlist': wishlist
        }

        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
