from rest_framework import viewsets, permissions

from asteroids_comets_meteors import serializers, models


class AsteroidCometMeteorViewSet(viewsets.ModelViewSet):
    """AsteroidCometMeteor Object API View"""
    serializer_class = serializers.AsteroidCometMeteorSerializer
    queryset = models.AsteroidCometMeteorObject.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
