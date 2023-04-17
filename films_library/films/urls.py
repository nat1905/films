"""Urls for app posts.
"""
from django.urls import path

from . import views

app_name = 'films'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('films/<int:film_id>/', views.film_reviews, name='film_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('create/', views.review_create, name='review_create'),
    
    path('film_create/', views.film_create, name='film_create'),
    path('films/', views.films, name='films'),
    path(
        'reviews/<int:review_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    
]
