from rest_framework import serializers

from messier_objects import models


class MessierSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes messier object data into useable form"""
    url = serializers.HyperlinkedIdentityField(
        view_name='messier-object-detail')

    class Meta:
        model = models.MessierObject
        fields = ('url',
                  'id',
                  'messier_number',
                  'name',
                  'ncg_or_ic_number',
                  'object_type',
                  'distance_kly',
                  'constellation',
                  'apparent_magnitude',
                  'photo',
                  'captured'
                  )
