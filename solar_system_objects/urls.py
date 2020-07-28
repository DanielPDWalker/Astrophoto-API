from django.urls import path, include
from rest_framework.routers import DefaultRouter

from solar_system_objects import views

router = DefaultRouter()
router.register('solar-system-object', views.SolarSystemViewSet,
                basename='solar-system-object')


urlpatterns = [
    path('', include(router.urls))
]
