from rest_framework import viewsets, permissions

from messier_objects import serializers, models


class MessierViewSet(viewsets.ModelViewSet):
    """Messier Object API View"""
    serializer_class = serializers.MessierSerializer
    queryset = models.MessierObject.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
