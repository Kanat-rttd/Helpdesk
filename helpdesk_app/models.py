from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Problem(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="new")
    # assigned_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # resolved_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name}, {self.priority}, {self.status}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



