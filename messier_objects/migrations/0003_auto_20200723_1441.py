# Generated by Django 2.2.9 on 2020-07-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messier_objects', '0002_auto_20200723_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messierobject',
            name='photo',
            field=models.ImageField(default='notcaptured.JPG', upload_to='messier_objects'),
        ),
    ]