from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form to review a product"""
    class Meta:
        model = Review
        fields = ('title', 'review_body', 'rating')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['review_body'].label = "Review"
