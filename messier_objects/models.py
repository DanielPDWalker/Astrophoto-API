from django.db import models


class MessierObject(models.Model):
    messier_number = models.CharField(max_length=4, required=True, unique=True)
    name = models.CharField(max_length=255, required=True)
    ncg_or_ic_number = models.CharField(max_length=25, required=True)
    object_type = models.CharField(max_length=255, required=True)
    distance_kly = models.CharField(max_length=25)
    constellation = models.CharField(required=True)
    apparent_magnitude = models.FloatField(required=True)
    right_ascension = models.CharField(max_length=50)
    declination = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='messier_objects', name=messier_number)
