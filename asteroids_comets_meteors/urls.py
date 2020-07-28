from django.urls import path, include
from rest_framework.routers import DefaultRouter

from asteroids_comets_meteors import views

router = DefaultRouter()
router.register('asteroid-comet-meteor', views.AsteroidCometMeteorViewSet,
                basename='asteroid-comet-meteor')


urlpatterns = [
    path('', include(router.urls))
]
