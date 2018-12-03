from django.db import models
from django.forms import ModelForm, CheckboxSelectMultiple

from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'releasedate', 'genres', 'directors']
    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['releasedate'].help_text = 'Format: YYYY-MM-DD'
        self.fields['genres'].help_text ='Hold down "Control" to select more than one'
        self.fields['directors'].help_text ='Hold down "Control" to select more than one'

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = ['name']

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class AddMovieToSeriesForm(ModelForm):
    class Meta:
        model = PartOfSeries
        fields = ['movie','number']

class AddStarToMovieForm(ModelForm):
    class Meta:
        model = Star
        fields = ['actor','role']