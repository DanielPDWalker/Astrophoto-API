# Generated by Django 3.0.8 on 2020-07-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_system_objects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarsystemobject',
            name='captured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='solarsystemobject',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='messier_objects'),
        ),
    ]
