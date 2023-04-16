"""Models for database
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

    
class Film(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)  
    year =  models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    
    film = models.ForeignKey(
        Film,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='comments'
    )

    class Meta:
        ordering = ['-pub_date', ]
