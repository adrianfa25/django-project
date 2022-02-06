from blog.models import Category, Movie, TvShow
from itertools import chain

# The itertools chain is to combine the 2 querysets from django.

def get_categories(request):

    categories_in_use_movies = Movie.objects.filter(public=True).values_list('categories', flat=True)

    categories_in_use_tvshows = TvShow.objects.filter(public=True).values_list('categories', flat=True)

    categories_in_use = chain(categories_in_use_movies, categories_in_use_tvshows)

    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')


    return {
        'categories': categories,
    }
