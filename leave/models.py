from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import timedelta

class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('hod_pending', 'Pending from HOD'),
        ('hod_approved', 'HOD Approved'),
        ('hod_rejected', 'HOD Rejected'),
        ('hr_pending', 'Pending HR Approval'),
        ('hr_approved', 'HR Approved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='hod_pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # No validation: allow all leave requests to be submitted
        pass

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ({self.start_date} to {self.end_date})"