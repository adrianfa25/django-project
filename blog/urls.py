from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.listmovie, name="list_movies"),
    path('tvshows/', views.listtvshow, name="list_tvshows"),
    path('category/<int:category_id>', views.category, name="category"),
    path('movie/<int:movie_id>', views.movie, name="movie"),
    path('tvshows/<int:tvshow_id>', views.tvshow, name="tvshow"),
    path('movies-and-tvshows/', views.listboth, name="movies-and-tvshows")

]
