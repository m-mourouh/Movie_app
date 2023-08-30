from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet, ReviewViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('actors', ActorViewSet, basename='actors')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = [
    
]

urlpatterns += router.urls