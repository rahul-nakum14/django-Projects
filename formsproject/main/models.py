from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name