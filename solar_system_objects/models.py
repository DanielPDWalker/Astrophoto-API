from django.db import models
from django.utils.text import slugify
from utils.slug_utils import unique_slugify


class SolarSystemObject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    object_type = models.CharField(max_length=255)
    parent_object = models.CharField(max_length=255, blank=True, null=True)
    distance_from_sun_au = models.FloatField(max_length=25, null=True)
    photo = models.ImageField(
        upload_to='solar_system_objects', blank=True, null=True)
    captured = models.BooleanField(default=False)
    capture_date = models.DateField(blank=True, null=True)

    def save(self, **kwargs):
        """Code found from :
        https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django
        """
        slug_str = "%s" % (self.name)
        unique_slugify(self, slug_str)
        super(SolarSystemObject, self).save(**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('distance_from_sun_au', )
