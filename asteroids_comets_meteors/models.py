from django.db import models


class AsteroidCometMeteorObject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    scientific_name = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    size_km = models.FloatField(max_length=255, blank=True, null=True)
    discovery_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='asteroid_comet_meteor', blank=True, null=True)
    captured = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.name + ' Scientific Name: ' + self.scientific_name
        except:
            return self.scientific_name

    class Meta:
        ordering = ('name',)
