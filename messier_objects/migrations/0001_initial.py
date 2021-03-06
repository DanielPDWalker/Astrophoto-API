# Generated by Django 2.2.9 on 2020-07-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessierObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messier_number', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('ncg_or_ic_number', models.CharField(max_length=25)),
                ('object_type', models.CharField(max_length=255)),
                ('distance_kly', models.CharField(max_length=25)),
                ('constellation', models.CharField(max_length=50)),
                ('apparent_magnitude', models.FloatField()),
                ('right_ascension', models.CharField(max_length=50)),
                ('declination', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='messier_objects')),
            ],
            options={
                'ordering': ('messier_number',),
            },
        ),
    ]
