from rest_framework import serializers
from .models import Computador, Periferico

class ComputadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computador
        fields = '__all__'

class PerifericoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periferico
        fields = '__all__'