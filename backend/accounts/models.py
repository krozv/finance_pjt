from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    birth_date = models.DateField(null=True, blank=True)
    real_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)