from django.db import models
from django.contrib import admin
from datetime import date

# Model declarations.
class Genre(models.Model):
    name = models.CharField("Genre Name",primary_key=True, max_length=64)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class Language(models.Model):
    name = models.CharField("Language Name", primary_key=True, max_length=64)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Person(models.Model):
    givenname = models.CharField("Given Name",max_length=128)
    surname = models.CharField("Surname", max_length=128)
    prefix = models.CharField("Prefix", max_length=64, blank=True)
    suffix = models.CharField("Suffix", max_length=64, blank=True)
    nameknownby = models.CharField("Name Known By", max_length=128, blank=True)
    is_director = models.BooleanField("Is Director", default=False)
    is_star = models.BooleanField("Is Actor", default=False)
    class Meta:
        ordering = ('nameknownby','prefix','surname','givenname','suffix')

    def __str__(self):
        if self.nameknownby:
            return self.nameknownby
        if self.suffix:
            return self.surname + ", " + self.givenname + ", " + self.suffix
        return self.surname + ", " + self.givenname

class Movie(models.Model):
    title = models.CharField(max_length=128)
    releasedate = models.DateField("Release Date")
    genres = models.ManyToManyField(Genre,blank=True)
    stars = models.ManyToManyField(
        Person,
        through='Star',
        related_name="star",
        blank=True}
    )
    directors = models.ManyToManyField(
        Person,
        related_name = "director",
        blank=True,
        limit_choices_to={'is_director':True}
    )

    class Meta:
        ordering = ('title','releasedate')

    def __str__(self):
        return self.title

class Star(models.Model):
    actor = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name ="acting_in",
        limit_choices_to={"is_star":True}
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)

    class Meta:
        unique_together = (("actor","movie","role"),)
        ordering = ('movie','actor','role')
    
    def __str__(self):
        return self.actor.__str__() + " as " + self.role + " in " + self.movie.title

class Series(models.Model):
    name = models.CharField(max_length=256)
    movies = models.ManyToManyField(Movie, through='PartOfSeries', blank=True)

    class Meta:
        verbose_name_plural="Series"
        ordering = ('name',)

    def __str__(self):
        return self.name

class PartOfSeries(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    number = models.FloatField("Number Order",null=True,blank=True)
    class Meta:
        verbose_name = "Series Belongs To"
        verbose_name_plural = "Series Belong To"
        unique_together = (("series","movie"),)
        ordering = ('series','number','movie')

class DVD(models.Model):
    name = models.CharField(max_length=256)
    movies = models.ManyToManyField(Movie)
    dateadded = models.DateField(default=date.today)
    version = models.CharField(max_length=64,blank=True)
    subtitle = models.ManyToManyField(Language, related_name ="subs",blank=True)
    audio = models.ManyToManyField(Language,related_name = "audio",blank=True)
    diskcondition = models.CharField(max_length=256,blank=True)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ('name','dateadded')

    def __str__(self):
        return self.name

# Admin Tools Inline Declarations

class StarInline(admin.TabularInline):
    model = Star
    extra = 2

class PartOfSeriesInline(admin.TabularInline):
    model = PartOfSeries
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = (StarInline,PartOfSeriesInline,)

class SeriesAdmin(admin.ModelAdmin):
    inlines = (PartOfSeriesInline,)
