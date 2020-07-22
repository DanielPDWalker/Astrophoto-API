from django.db import models


class MessierObject(models.Model):
    messier_number = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)
    ncg_or_ic_number = models.CharField(max_length=25)
    object_type = models.CharField(max_length=255)
    distance_kly = models.CharField(max_length=25)
    constellation = models.CharField(max_length=50)
    apparent_magnitude = models.FloatField()
    right_ascension = models.CharField(max_length=50)
    declination = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='messier_objects')

    def __str__(self):
        return self.messier_number + ': ' + self.name

    class Meta:
        ordering = ('messier_number', )
