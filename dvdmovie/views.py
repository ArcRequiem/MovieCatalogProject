from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *
# Create your views here.

def index(request):
    latest_movie_list = Movie.objects.order_by('-id')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie':movie
    }
    return render(request, 'movies/detail.html', context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST or None)
        if form.is_valid():
            movie=form.save()
            return HttpResponseRedirect(reverse("movies:movie_detail",  args=(movie.id,)))
    else:
        form = MovieForm()
    return render(request, 'movies/addmovie.html', {'form':form,})

def edit_movie(request, movie_id=None):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST' and 'save-btn' in request.POST:
        form = MovieForm(request.POST or None, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("movies:movie_detail",  args=(movie_id,)))
    elif request.method =='POST' and 'delete-btn' in request.POST:
        Movie.objects.filter(pk=movie_id).delete()
        return HttpResponseRedirect(reverse("movies:movie_list"))
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/editform.html', {'form':form,'movie':movie})

def listing(request):
    movie_list = Movie.objects.all
    context = {'movie_list':movie_list}
    return render(request, 'movies/list.html', context)

def add_actor(request, movie_id=None):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = AddStarToMovieForm(request.POST or None)
        if form.is_valid():
            try:
                star = form.save(commit=False)
                star.movie = movie
                star.save()
                return HttpResponseRedirect(reverse("movies:movie_detail",  args=(movie_id,)))
            except:
                return HttpResponseRedirect(reverse("movies:movie_detail",  args=(movie_id,)))
    else:
        form = AddStarToMovieForm()
    return render(request, 'movies/moviestarform.html', {'form':form,'movie':movie})

def delete_actor(request, movie_id=None, star_id=None):
    star=get_object_or_404(Star,pk=star_id)
    movie=get_object_or_404(Movie,pk=movie_id)
    star.delete()
    return HttpResponseRedirect(reverse("movies:movie_detail", args=(movie_id,)))

def movie_search(request):
    if request.GET.get('cs') == 'series':
        return series_search(request)
    if request.GET.get('cs') == 'person':
        return person_search(request)
    keyword=request.GET.get('q')
    search_list = Movie.objects.filter(title__icontains=keyword)
    context = {
        'keyword': keyword,
        'search_list': search_list
    }
    return render(request,'movies/search.html', context)

def series(request):
    series_list = Series.objects.all
    context = {'series_list':series_list}
    return render(request,'series/list.html', context)

def series_detail(request, series_id=None):
    series = get_object_or_404(Series, pk=series_id)
    movies = series.partofseries_set.order_by('number')
    context = {
        'series': series,
        'movies': movies,
    }
    return render(request, 'series/detail.html', context)

def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST or None)
        if form.is_valid():
            series=form.save()
            return HttpResponseRedirect(reverse("movies:series_detail",  args=(series.id,)))
    else:
        form = SeriesForm()
    return render(request, 'series/addseries.html', {'form':form,})


def edit_series(request, series_id=None):
    series = get_object_or_404(Series, pk=series_id)
    if request.method == 'POST' and 'save-btn' in request.POST:
        form = SeriesForm(request.POST or None, instance=series)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("movies:series_detail",  args=(series_id,)))
    elif request.method =='POST' and 'delete-btn' in request.POST:
        Series.objects.filter(pk=series_id).delete()
        return HttpResponseRedirect(reverse("movies:series_list"))
    else:
        form = SeriesForm(instance=series)
    return render(request, 'series/editform.html', {'form':form,'series':series})

def series_add_movie(request, series_id=None):
    series = get_object_or_404(Series, pk=series_id)
    if request.method == 'POST':
        form = AddMovieToSeriesForm(request.POST or None)
        if form.is_valid():
            try:
                partofseries = form.save(commit=False)
                partofseries.series = series
                partofseries.save()
                return HttpResponseRedirect(reverse("movies:series_detail",  args=(series_id,)))
            except:
                return HttpResponseRedirect(reverse("movies:series_detail",  args=(series_id,)))
    else:
        form = AddMovieToSeriesForm()
    return render(request, 'series/addmovie.html', {'form':form,'series':series})

def series_delete_movie(request, series_id=None, movie_id=None):
    series=get_object_or_404(Series,pk=series_id)
    movie=get_object_or_404(Movie,pk=movie_id)
    PartOfSeries.objects.filter(series=series).filter(movie=movie).delete()
    return HttpResponseRedirect(reverse("movies:series_detail", args=(series_id,)))

def series_search(request):
    if request.GET.get('cs') == 'movie':
        return movie_search(request)
    if request.GET.get('cs') == 'person':
        return person_search(request)
    keyword = request.GET.get('q')
    search_list = Series.objects.filter(name__icontains=keyword)
    context = {
        'keyword': keyword,
        'search_list': search_list
    }
    return render(request,'series/search.html', context)

def person(request):
    person_list = Person.objects.all
    context = {'person_list':person_list}
    return render(request,'person/list.html', context)

def person_detail(request, person_id=None):
    person = get_object_or_404(Person, pk=person_id)
    movies = person.acting_in.order_by('-movie__releasedate')
    context = {
        'person': person,
        'movies': movies,
    }
    return render(request, 'person/detail.html', context)

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST or None)
        if form.is_valid():
            person=form.save()
            return HttpResponseRedirect(reverse("movies:person_detail",  args=(person.id,)))
    else:
        form = PersonForm()
    return render(request, 'person/addperson.html', {'form':form,})


def edit_person(request, person_id=None):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST' and 'save-btn' in request.POST:
        form = PersonForm(request.POST or None, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("movies:person_detail",  args=(person_id,)))
    elif request.method =='POST' and 'delete-btn' in request.POST:
        Person.objects.get(pk=person_id).delete()
        return HttpResponseRedirect(reverse("movies:person_list"))
    else:
        form = PersonForm(instance=person)
    return render(request, 'person/editform.html', {'form':form,'person':person})

def person_search(request):
    if request.GET.get('cs') == 'movie':
        return movie_search(request)
    elif request.GET.get('cs') == 'series':
        return series_search(request)
    keyword = request.GET.get('q')
    snfilter=Person.objects.filter(surname__icontains = keyword)
    gnfilter=Person.objects.filter(givenname__icontains = keyword)
    sffilter=Person.objects.filter(suffix__icontains = keyword)
    nkbfilter=Person.objects.filter(surname__icontains = keyword)
    search_list = snfilter.union(gnfilter).union(sffilter).union(nkbfilter)
    context = {
        'keyword': keyword,
        'search_list': search_list
    }
    return render(request,'person/search.html', context)
