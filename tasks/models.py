from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class user_details(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    c_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,max_length=250)
    progress = models.CharField(max_length=100,default='InProgress')
    time = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

