from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, ActorSerializer
from .models import Movie, Actor


# Movie ViewSet
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
# Actor ViewSet
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer