from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()
# Create your models here.
class Pizza(models.Model):
    name = models.CharField(
        max_length=30
    )
    price = models.FloatField(validators=[MinValueValidator(0)])
    image_url = models.URLField()
    calories = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

class Like(models.Model):
    pizza =models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user=models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )