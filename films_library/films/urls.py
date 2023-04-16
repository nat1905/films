"""Urls for app posts.
"""
from django.urls import path

from . import views

app_name = 'films'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('films/<int:film_id>/', views.film_comments, name='film_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('create/', views.comment_create, name='comment_create'),
    
    path('film_create/', views.film_create, name='film_create'),
    path('films/', views.films, name='films'),
    
]
