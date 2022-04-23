from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    profile_picture = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)