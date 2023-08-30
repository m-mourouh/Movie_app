from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet, ReviewViewSet, addMovieActor, removeMovieActor, movieReviews

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('actors', ActorViewSet, basename='actors')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = [
        path('movie/<str:id>/actor', addMovieActor, name="add-movie-actor"),
        path('movie/<str:id>/actor/<str:pk>', removeMovieActor, name="remove-movie-actor"),
        path('movie-reviews/<str:id>', movieReviews, name="movie-reviews"),
]

urlpatterns += router.urls