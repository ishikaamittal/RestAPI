from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class records(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    weight = models.CharField( default=1)
    length = models.IntegerChoices( default=1)
    timestamp = models.DateTimeField(default=False)
    latitude = models.FloatField(min_value=-90, max_value=90)
    longitude = models.FloatField(min_value=-180, max_value=180)
    image = models.ImageField(upload_to='image')

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
