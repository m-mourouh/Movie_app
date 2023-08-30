from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('actors', ActorViewSet, basename='actors')

urlpatterns = [
    
]

urlpatterns += router.urls