from re import search
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Records
# from .tasks import file_resize

class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    fields = ('name','species','weight','height','file', 'timestamp','latitude','longitude')

    # def save(self, commit=True):
    #   records = super().save(commit)
    #   file_resize.apply_async((records.id))
    #   return records