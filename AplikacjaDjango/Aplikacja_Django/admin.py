from django.contrib import admin
from .models import Movie, Rating, Actor, Director


class MoviePanel(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'actors', 'director')
    list_display = ('title', 'no_of_ratings', 'mean_rating', 'updated', 'created')


class RatingPanel(admin.ModelAdmin):
    list_display = ('movie', 'user', 'stars')


class ActorPanel(admin.ModelAdmin):
    fields = ('name', 'surname')


class DirectorPanel(admin.ModelAdmin):
    fields = ('name', 'surname')


admin.site.register(Movie, MoviePanel)
admin.site.register(Rating, RatingPanel)
admin.site.register(Actor, ActorPanel)
admin.site.register(Director, DirectorPanel)
