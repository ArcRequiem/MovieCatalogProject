from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='movie_index'),
    path('movie/', views.listing, name='movie_list'),
    path('movie/add/', views.add_movie, name='movie_add'),
    path('movie/<int:movie_id>/', views.detail, name='movie_detail'),
    path('movie/<int:movie_id>/edit/', views.edit_movie, name='movie_edit'),
    path('movie/<int:movie_id>/addactor/', views.add_actor, name='movie_add_actor'),
    path('movie/<int:movie_id>/deleteactor/<int:star_id>/', views.delete_actor, name='movie_delete_actor'),
    path('movie/search/', views.movie_search, name='movie_search'),
    path('series/', views.series, name='series_list'),
    path('series/add/', views.add_series, name='series_add'),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    path('series/<int:series_id>/edit/', views.edit_series, name='series_edit'),
    path('series/<int:series_id>/addmovie/', views.series_add_movie, name='series_add_movie'),
    path('series/<int:series_id>/deletemovie/<int:movie_id>/', views.series_delete_movie, name='series_delete_movie'),
    path('series/search/', views.series_search, name='series_search'),
    path('person/', views.person, name='person_list'),
    path('person/add/', views.add_person, name='person_add'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
    path('person/<int:person_id>/edit/', views.edit_person, name='person_edit'),
    path('person/search/', views.person_search, name='person_search'),
]
