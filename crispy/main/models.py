from django.db import models
from django.contrib.auth.models import User

class post_model(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title + "\n" + self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='pics')
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'