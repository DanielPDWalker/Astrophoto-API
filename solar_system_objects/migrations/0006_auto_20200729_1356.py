# Generated by Django 3.0.8 on 2020-07-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_system_objects', '0005_auto_20200729_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarsystemobject',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
