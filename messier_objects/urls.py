from django.urls import path, include
from rest_framework.routers import DefaultRouter

from messier_objects import views

router = DefaultRouter()
router.register('messier-object', views.MessierViewSet,
                basename='messier-object')


urlpatterns = [
    path('', include(router.urls))
]
