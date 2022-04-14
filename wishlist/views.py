from django.shortcuts import render


def wishlist(request):
    """Show wishlist"""

    template = 'wishlist/wishlist.html'
    return render(request, template)
