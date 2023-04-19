"""Forms for app Post.
"""
from django import forms

from .models import Review, Film, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'film')
        labels = {
            'text': 'Text of the review',            
            'film': 'Review is about the film'
        }
        

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film     
        fields = ('title', 'director', 'year', 'description', 'image_film')
        labels = {
            'title': 'Film title',
            'director': 'Director  of the film', 
            'year': 'Year format: 2022-01-01',           
            'description' : 'Description of the film',
            'image_film': 'Upload image'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        
