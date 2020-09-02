from django.db import models


# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=20)
    link = models.URLField(max_length=200)
    userId = models.IntegerField()

