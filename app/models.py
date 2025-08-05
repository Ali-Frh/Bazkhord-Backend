from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Optional extra fields
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
