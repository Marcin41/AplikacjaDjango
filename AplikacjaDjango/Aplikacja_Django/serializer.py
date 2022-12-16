from .models import Actor, Director, Movie, Rating
from rest_framework import serializers
from django.contrib.auth.models import User


class ActorSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'surname']


class DirectorSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'surname']


class MovieSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'slug', 'description', 'actors', 'director', 'created', 'updated', 'no_of_ratings', 'mean_rating']


class RatingSerializer (serializers.HyperlinkedModelSerializer):
    movie = MovieSerializer(many=False)


    class Meta:
        model = Rating
        fields = ['movie', 'user', 'stars']
