from django.db import models


class MessierObject(models.Model):
    messier_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    ncg_or_ic_number = models.CharField(max_length=25)
    object_type = models.CharField(max_length=255)
    distance_kly = models.CharField(max_length=25)
    constellation = models.CharField(max_length=50)
    apparent_magnitude = models.FloatField()
    photo = models.ImageField(
        upload_to='messier_objects', blank=True, null=True)
    captured = models.BooleanField(default=False)

    def __str__(self):
        return 'M' + str(self.messier_number) + ': ' + self.name

    class Meta:
        ordering = ('messier_number', )
