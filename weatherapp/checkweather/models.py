from django.utils.text import slugify
from django.db import models


# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.city_name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.city_name