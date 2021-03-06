# Generated by Django 3.0.8 on 2020-07-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asteroids_comets_meteors', '0004_auto_20200728_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='asteroidcometmeteorobject',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='asteroidcometmeteorobject',
            name='scientific_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
