from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Reviews list in Admin """
    list_display = (
        'title',
        'product',
        'user',
        'rating',
        'date_posted'
    )
