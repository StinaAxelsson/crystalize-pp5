from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

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

            reviews = Review.objects.filter(product=product)
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = int(avg_rating)
            product.save()
            messages.success(request, 'Thank you for your Review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oops, something went wrong! \
                Please try again.')

        context = {
            'form': form,
        }

    return render(request, context)


@login_required
def delete_review(request, review_id):
    """
    Delete a review by the logged in user who wrote it.
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review is now deleted!')
    return redirect(reverse('product_detail', args=(review.product.id,)))
