from .models import Launche
from rest_framework import serializers


class LauncheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launche
        fields = '__all__'
