"""Admin part for app posts.

"""
from django.contrib import admin

from .models import Review, Film, Comment


class FilmAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'director', 'year', 'description')
    search_fields = ('title', 'director',)
    list_filter = ('title', 'director',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author',  'film')
    list_editable = ('film',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'author', 'review')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Review, ReviewAdmin)
