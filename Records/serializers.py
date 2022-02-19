from re import search
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import records

class recordsSeralizer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    species = serializers.CharField(max_length=50)
    weight=serializers.DecimalField(max_digits=30,decimal_places=1)
    height=serializers.DecimalField(max_digits=20,decimal_places=1)
    timestamp = serializers.DateTimeField(default=False)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    image = serializers.ImageField()

    class Meta:
        model = records
        fields = ('__all__')