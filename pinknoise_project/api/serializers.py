from rest_framework import serializers
from .models import PinkNoise

class PinkNoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinkNoise
        fields = '__all__'