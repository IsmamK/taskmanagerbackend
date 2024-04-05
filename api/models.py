from django.db import models
from django.contrib.auth.models import User  # Import the User model
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a foreign key to the User model
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed')
    )
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="pending")
    def __str__(self):
        return self.title