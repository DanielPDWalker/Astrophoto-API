from rest_framework import serializers

from solar_system_objects import models


class SolarSystemSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes messier object data into useable form"""
    url = serializers.HyperlinkedIdentityField(
        view_name='solar-system-object-detail')

    class Meta:
        model = models.SolarSystemObject
        fields = ('url',
                  'id',
                  'name',
                  'object_type',
                  'parent_object',
                  'distance_from_sun_au',
                  'photo'
                  )
