# Generated by Django 2.2.9 on 2020-07-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messier_objects', '0003_auto_20200723_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messierobject',
            name='photo',
            field=models.ImageField(blank=True, default='notcaptured.JPG', upload_to='messier_objects'),
        ),
    ]
