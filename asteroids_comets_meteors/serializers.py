from rest_framework import serializers

from asteroids_comets_meteors import models


class AsteroidCometMeteorSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes asteroid, comet and meteor data into useable form"""
    url = serializers.HyperlinkedIdentityField(
        view_name='asteroid-comet-meteor-detail')

    class Meta:
        model = models.AsteroidCometMeteorObject
        fields = ('url',
                  'id',
                  'name',
                  'scientific_name',
                  'object_type',
                  'size_km',
                  'discovery_date',
                  'photo',
                  'captured'
                  )
