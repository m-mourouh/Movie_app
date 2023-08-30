from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer
from .models import Movie, Actor, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


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

# add -> new actor ->  movie
@api_view(["POST"])
def addMovieActor(request, id):
    movie = Movie.objects.filter(id=id).first()
    actor = Actor.objects.filter(first_name=request.data["first_name"], last_name=request.data["last_name"])
    actorSerializer = ActorSerializer(data= request.data, many=False)
    movieSerializer = MovieSerializer(movie, many=False)
    
     # check if  actor already exists + valid serializer
    try:
        if actorSerializer.is_valid() and not actor.exists():
            actorSerializer.save()
            actor = Actor.objects.get(id=actorSerializer.data["id"])
            movie.actors.add(actor)
            
        movie_actor = movie.actors.filter(first_name=request.data["first_name"], last_name=request.data["last_name"])
        
        if  not movie_actor.exists() and actor.exists():
            actor = Actor.objects.get(id=actor.first().id)
            movie.actors.add(actor)
            
    except ObjectDoesNotExist:
        print("Actor dosn't exist ")
        
    return Response(movieSerializer.data)

# delete ->  actor ->  movie
@api_view(["DELETE"])
def removeMovieActor(request, id, pk):
    movie = Movie.objects.filter(id=id).first()
     # check if actor already exists
    actor = Actor.objects.filter(id=pk,first_name=request.data["first_name"], last_name=request.data["last_name"])
    serializer = MovieSerializer(movie, many=False)
    
    if actor.exists():
        movie.actors.remove(actor.first())
        
    return Response(serializer.data)

# Get movie reviews 
@api_view(["GET"])
def movieReviews(request, id):
    reviews = Review.objects.filter(movie=id)
    serializer = ReviewSerializer(reviews, many=True)
    
    return Response(serializer.data)