# Generated by Django 3.1.3 on 2020-11-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkweather', '0003_auto_20201127_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
