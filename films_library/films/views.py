"""Views for app films.
"""
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FilmForm, ReviewForm
from .models import Film, Review, User


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
    reviews = Review.objects.all()
    paginator = Paginator(reviews, PAGES_NUMBER)
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





def film_reviews(request, film_id):
    """Film page.
    """
    template = 'films/film_list.html'
    title = f'reviews about {get_object_or_404(Film, pk=film_id)}'
    film = get_object_or_404(Film, pk=film_id)
    reviews = film.reviews.all()
    paginator = Paginator(reviews, PAGES_NUMBER)
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
    reviews = author.reviews.all()
    author_equel_user = user_author(request, author)
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'author': author,
        'num_review_list': reviews.count,
        'page_obj': page_obj,
        'author_equel_user': author_equel_user
    }
    return render(request, 'films/profile.html', context)


def review_detail(request, review_id):
    """Review page.
    """
    review = get_object_or_404(Review, pk=review_id)
    num_reviews = Review.objects.filter(author__username=review.author).count()
    author_equel_user = user_author(request, review.author)

    context = {
        'review': review,
        'num_review_list': num_reviews,
        'author_equel_user': author_equel_user
    }
    return render(request, 'films/review_detail.html', context)


@login_required
def review_create(request):
    """review create page.
    """
    form = ReviewForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'films/review_create.html', {'form': form})
    review = form.save(commit=False)
    review.author = request.user
    review.save()
    return redirect('films:profile', review.author.username)

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


