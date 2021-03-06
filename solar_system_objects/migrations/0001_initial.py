# Generated by Django 3.0.8 on 2020-07-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolarSystemObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('object_type', models.CharField(max_length=255)),
                ('parent_object', models.CharField(max_length=255)),
                ('distance_from_sun_au', models.FloatField(max_length=25)),
                ('photo', models.ImageField(blank=True, default='notcaptured.JPG', null=True, upload_to='messier_objects')),
            ],
            options={
                'ordering': ('distance_from_sun_au',),
            },
        ),
    ]
