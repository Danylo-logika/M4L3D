from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=60)
    text = models.TextField()
    date = models.DateTimeField()
