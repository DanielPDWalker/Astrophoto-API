# Generated by Django 3.0.8 on 2020-07-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messier_objects', '0008_auto_20200728_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messierobject',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]