from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form to review a product"""
    class Meta:
        model = Review
        fields = ('rating', 'review_body')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['review_body'].label = "Review"
