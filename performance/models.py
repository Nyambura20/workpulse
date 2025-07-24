from django.db import models
from django.contrib.auth.models import User

class PerformanceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField()
    rating = models.CharField(max_length=20)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.year} - {self.rating}"
