from rest_framework import serializers
from .models import Clothes

class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ('name','image','price', 'description')