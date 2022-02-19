from distutils.command.upload import upload
from django.db import models

# Create your models here.
class records(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight=models.DecimalField(max_digits=30,decimal_places=1)
    height=models.DecimalField(max_digits=20,decimal_places=1)
    timestamp = models.DateTimeField(default=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='image')

   