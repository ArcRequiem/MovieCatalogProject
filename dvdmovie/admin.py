from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Person)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Language)
admin.site.register(Star)