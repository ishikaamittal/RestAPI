from distutils.command.upload import upload
from django.db import models
from PIL import Image

class Records(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=30, decimal_places=1)
    height = models.DecimalField(max_digits=20, decimal_places=1)
    file = models.FileField(blank=False, null=False)
    is_cropped = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def get_species(self):
        return self.name + ' belongs to ' + self.species + ' species.'