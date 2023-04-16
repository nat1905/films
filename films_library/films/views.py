"""Views for app posts.
"""
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FilmForm, CommentForm
from .models import Film, Comment, User


PAGES_NUMBER = 10


def user_author(request, author):
    if request.user != author:
        return False
    return True


def index(request):
    """Main page.
    """
    template = 'films/index.html'
    title = 'Last changes.'
    comments = Comment.objects.all()
    paginator = Paginator(comments, PAGES_NUMBER)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def films(request):
    """All films.
    """
    template = 'films/films.html'
    title = 'All films.'
    films = Film.objects.all()
    paginator = Paginator(films, PAGES_NUMBER)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)





def film_comments(request, film_id):
    """Film page.
    """
    template = 'films/film_list.html'
    title = f'Comments about {get_object_or_404(Film, pk=film_id)}'
    film = get_object_or_404(Film, pk=film_id)
    comments = film.comments.all()
    paginator = Paginator(comments, PAGES_NUMBER)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'film': film,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    """Author page.
    """
    title = (
        f'Профайл пользователя '
        f'{get_object_or_404(User, username=username)}'
    )
    author = get_object_or_404(User, username=username)
    comments = author.comments.all()
    author_equel_user = user_author(request, author)
    paginator = Paginator(comments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'author': author,
        'num_comment_list': comments.count,
        'page_obj': page_obj,
        'author_equel_user': author_equel_user
    }
    return render(request, 'films/profile.html', context)


def comment_detail(request, comment_id):
    """comment page.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    num_comments = Comment.objects.filter(author__username=comment.author).count()
    author_equel_user = user_author(request, comment.author)

    context = {
        'comment': comment,
        'num_comment_list': num_comments,
        'author_equel_user': author_equel_user
    }
    return render(request, 'films/comment_detail.html', context)


@login_required
def comment_create(request):
    """comment create page.
    """
    form = CommentForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'films/comment_create.html', {'form': form})
    comment = form.save(commit=False)
    comment.author = request.user
    comment.save()
    return redirect('films:profile', comment.author.username)

@login_required
def film_create(request):
    """Film create page.
    """
    form = FilmForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'films/film_create.html', {'form': form})
    film = form.save(commit=False) 
    film.author = request.user   
    film.save()
    return redirect('films:profile', film.author.username)


