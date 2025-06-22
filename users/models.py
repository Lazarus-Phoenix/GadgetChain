from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    position = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"