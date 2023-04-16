"""Forms for app Post.
"""
from django import forms

from .models import Comment, Film


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'film')
        labels = {
            'text': 'Text of the post',            
            'film': 'Comment is about the film'
        }
        

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film     
        fields = ('title', 'director', 'year', 'description')
        labels = {
            'title': 'Film title',
            'director': 'director  of the film', 
            'year': 'year',           
            'description' : 'Description of the film'
        }
        
