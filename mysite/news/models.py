from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=256)
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title