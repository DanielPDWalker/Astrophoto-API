from django.db import models


class SolarSystemObject(models.Model):
    name = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    parent_object = models.CharField(max_length=255)
    distance_from_sun_au = models.FloatField(max_length=25)
    photo = models.ImageField(
        upload_to='messier_objects', blank=True, null=True, default='notcaptured.JPG')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('distance_from_sun_au', )
