from django.db import models
from django.contrib.auth.models import User


class registration(models.Model):
    name = models.CharField(max_length=10)
    email  = models.EmailField()
    password = models.TextField()
    confirmpassword = models.TextField()

