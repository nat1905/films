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
    image_film = models.ImageField(
        'Image',
        upload_to='films/',
        blank=True
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    film = models.ForeignKey(
        Film,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='reviews'
    )

    class Meta:
        ordering = ['-pub_date', ]

class Comment(models.Model):
    text = models.TextField(verbose_name='Text')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Date'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Author'
    )
    review = models.ForeignKey(
        Review,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='comments',
        verbose_name='Review'
    )

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return self.text[:15]
