from django.db import models

# Create your models here.
class RSS_Item(models.Model):
    image           =   models.ImageField()
    published_date  =   models.DateField()
    title           =   models.CharField(max_length=255)
    description     =   models.CharField(max_length=255)
    url             =   models.URLField()