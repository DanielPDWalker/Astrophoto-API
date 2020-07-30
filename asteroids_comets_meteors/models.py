from django.db import models
from django.utils.text import slugify
from utils.slug_utils import unique_slugify


class AsteroidCometMeteorObject(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True)
    scientific_name = models.CharField(max_length=255)
    object_type = models.CharField(max_length=255)
    size_km = models.FloatField(max_length=255, blank=True, null=True)
    discovery_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='asteroid_comet_meteor', blank=True, null=True)
    captured = models.BooleanField(default=False)
    capture_date = models.DateField(blank=True, null=True)

    def save(self, **kwargs):
        """Code found from :
        https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django
        """
        slug_str = "%s" % (self.scientific_name)
        unique_slugify(self, slug_str)
        super(AsteroidCometMeteorObject, self).save(**kwargs)

    def __str__(self):
        try:
            return self.name + ' Scientific Name: ' + self.scientific_name
        except:
            return self.scientific_name

    class Meta:
        ordering = ('name',)
