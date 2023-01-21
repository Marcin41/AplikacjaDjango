from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class Actor(models.Model):
        name = models.CharField(max_length=16, null=False, blank=False)
        surname = models.CharField(max_length=16, null=False, blank=False)

        class Meta:
            index_together = (('name', 'surname'),)

        def __str__(self):
            return "{} {}".format(self.name, self.surname)


class Director(models.Model):
        name = models.CharField(max_length=16, null=False, blank=False)
        surname = models.CharField(max_length=16, null=False, blank=False)

        class Meta:
            index_together = (('name', 'surname'),)

        def __str__(self):
            return "{} {}".format(self.name, self.surname)


class Movie(models.Model):
        title = models.CharField(max_length=32, null=False, blank=False, unique=True)
        slug = models.SlugField(max_length=40)
        description = models.TextField(max_length=360)
        actors = models.ManyToManyField(Actor)
        director = models.ManyToManyField(Director)
        created = models.DateField(auto_now_add=True, blank=True, null=True)
        updated = models.DateField(blank=False, null=False, auto_now=True)

        def __str__(self):
            return "{}".format(self.title)

        def no_of_ratings(self):
            ratings = Rating.objects.filter(movie=self)
            return len(ratings)

        def mean_rating(self):
            ratings = Rating.objects.filter(movie=self)
            suma = 0
            mean = 0
            for rating in ratings:
                suma = suma + rating.stars
            if suma != 0:

                mean = suma / len(ratings)

                return mean
            else:

                return mean


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False, null=False)


    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

    def __str__(self):
        return "{} {}".format(self.user, self.stars)
