from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)  #many to many relationship
    
    def __str__(self):
        return self.title

    
    
class Review(models.Model):
    grade = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(0)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  #One to many relationship
    
    def __str__(self):
        return f'{self.movie.title} {self.grade}'