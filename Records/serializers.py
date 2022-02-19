from re import search
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Records

class RecordSerializer(serializers.ModelSerializer):
  class Meta():
    model = Records
    fields = ('name','species','weight','height','file', 'timestamp','latitude','longitude')