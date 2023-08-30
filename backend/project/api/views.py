from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer
from .models import Movie, Actor, Review


# Movie ViewSet
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
# Actor ViewSet
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer