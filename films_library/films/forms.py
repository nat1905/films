"""Forms for app Post.
"""
from django import forms

from .models import Review, Film


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'film')
        labels = {
            'text': 'Text of the post',            
            'film': 'Review is about the film'
        }
        

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film     
        fields = ('title', 'director', 'year', 'description')
        labels = {
            'title': 'Film title',
            'director': 'Director  of the film', 
            'year': 'Year format: 2022-01-01',           
            'description' : 'Description of the film'
        }
        
