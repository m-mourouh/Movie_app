from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet, ReviewViewSet, addMovieActor

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('actors', ActorViewSet, basename='actors')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = [
        path('movie/<str:id>/actor', addMovieActor, name="add-movie-actor"),
]

urlpatterns += router.urls