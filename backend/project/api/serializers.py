from rest_framework import serializers
from .models import Movie, Review, Actor


class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
            depth = 1
            

            
class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'
            
        
class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'