from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(
        max_length=30
    )
    price = models.FloatField(validators=[MinValueValidator(0)])
    image_url = models.URLField()
    calories = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)