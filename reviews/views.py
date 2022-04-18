from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """ View for users to add a review on a product """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            messages.success(request, 'Thank you for your Review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oops, something went wrong! \
                Please try again.')

    context = {
        'form': form,
    }

    return render(request, context)
