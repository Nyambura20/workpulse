
from django.db import models
from django.contrib.auth.models import User

class HODProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any HOD-specific fields here

    def __str__(self):
        return f"HOD: {self.user.username}"
