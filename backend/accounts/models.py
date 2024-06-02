from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # 커스텀 필드 추가
    birth_date = models.DateField(null=True, blank=True)
    real_name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)