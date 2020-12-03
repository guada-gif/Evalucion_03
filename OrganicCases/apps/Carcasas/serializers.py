from rest_framework import serializers
from .models import Carcasa, Material


class CarcasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carcasa
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
