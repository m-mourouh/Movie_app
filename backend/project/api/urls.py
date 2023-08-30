from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')

urlpatterns = [
    
]

urlpatterns += router.urls