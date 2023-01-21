from .models import Actor, Director, Movie, Rating
from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User


class ActorSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname']

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('Name')
            surname = request.data.get('Surname')
            actor = Actor.objects.create(Name=name, Surname=surname)
            serializer = ActorSerializer(actor, many=False)
            response = {'Actor added ': serializer.data}
            return Response(response,status=status.HTTP_201_CREATED)
        except:
            response = {'Something went wrong'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class DirectorSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'surname']

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('Name')
            surname = request.data.get('Surname')
            director = Director.objects.create(Name=name, Surname=surname)
            serializer = ActorSerializer(director, many=False)
            response = {'Director added ': serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        except:
            response = {'Something went wrong'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MovieSerializer (serializers.HyperlinkedModelSerializer):
    actors = ActorSerializer(many=True)
    director = DirectorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'slug', 'description', 'actors', 'director', 'created', 'updated', 'no_of_ratings', 'mean_rating']


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class RatingSerializer (serializers.HyperlinkedModelSerializer):
    movie = MovieSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Rating
        fields = ['id', 'movie', 'user', 'stars']