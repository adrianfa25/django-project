from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Movie, TvShow
from django.contrib.auth.decorators import login_required
from itertools import chain



@login_required(login_url='login')
def listmovie(request):
        #sacar articulos
        movies = Movie.objects.filter(public=True)

        #paginar los artiuclos
        paginator = Paginator(movies, 4)

        #recoger numero pagina
        page = request.GET.get('page')
        page_movies = paginator.get_page(page)

        return render(request, 'movies/list.html',{
                'title':'Movies',
                'movies': page_movies
} )


@login_required(login_url='login')
def listtvshow(request):
        #sacar articulos
        tvshows = TvShow.objects.filter(public=True)

        #paginar los artiuclos
        paginator = Paginator(tvshows, 4)

        #recoger numero pagina
        page = request.GET.get('page')
        page_tvshows = paginator.get_page(page)

        return render(request, 'tvshows/list.html',{
                'title':'Tv Shows',
                'tvshows': page_tvshows
} )


#Page fot both articles (movies and tvshows)
@login_required(login_url='login')
def listboth(request):
        #sacar articulos
        movies = Movie.objects.filter(public=True) 
        tvshows = TvShow.objects.filter(public=True)

        return render(request, 'movies-and-tvshows/list.html',{
                'title':'Movies and Tv Shows',
                'movies': movies,
                'tvshows': tvshows
        })



def category(request, category_id):
        category = get_object_or_404(Category, id=category_id)
        movies = Movie.objects.filter(categories=category)
        tvshows = TvShow.objects.filter(categories=category)

        return render(request, 'categories/category.html', {
                'category': category,
                'movies': movies,
                'tvshows': tvshows

        })

def movie(request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        return render(request, 'movies/details.html', {
                'movie': movie
        })


def tvshow(request, tvshow_id):
        tvshow = get_object_or_404(TvShow, id=tvshow_id)

        return render(request, 'tvshows/details.html', {
                'tvshow': tvshow
        })