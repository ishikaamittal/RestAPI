from distutils.command.upload import upload
from django.db import models
from PIL import Image

class Records(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=30, decimal_places=1)
    height = models.DecimalField(max_digits=20, decimal_places=1)
    file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def save_file(self,*args, **kwargs):
        super().save_file(*args, **kwargs)

        img = Image.open(self.file.path)

        if img.height > 300 or img.width > 300:
            output_size = (140, 140)
            img.thumbnail(output_size)
            img.save_file(self.file.path)
