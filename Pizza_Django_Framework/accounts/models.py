from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from Pizza_Django_Framework.accounts.managers import PizzaUserManager


class PizzaUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)

    is_staff =models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'email'

    objects =PizzaUserManager()

class Profile(models.Model):
    profile_image=models.URLField(
        blank=True
    )
    user =models.OneToOneField(
        PizzaUser,
        on_delete=models.CASCADE,
        primary_key =True,
    )

from .signals import *