from rest_framework import viewsets, permissions

from solar_system_objects import serializers, models


class SolarSystemViewSet(viewsets.ModelViewSet):
    """Solar System Object API View"""
    serializer_class = serializers.SolarSystemSerializer
    queryset = models.SolarSystemObject.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
