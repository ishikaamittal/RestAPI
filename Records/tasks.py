from celery import shared_task
from .models import Records
from zipfile import ZipFile
from PIL import Image
import os
from django.conf import settings

@shared_task
def resizing():
    uncropped_records = Records.objects.filter(is_cropped=False)
    for record in uncropped_records:
        img = Image.open(record.file.path)  
        output_size = (140, 140)
        img.thumbnail(output_size)
        img.save(record.file.path)
        record.is_cropped = True
        record.save()
        print(record.is_cropped)
        return img

