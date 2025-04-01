from django import forms
from .models import CrimeShow, Review

class CrimeShowForm(forms.ModelForm):
    class Meta:
        model = CrimeShow
        fields = ['title', 'description', 'genre', 'release_date', 'rating', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
