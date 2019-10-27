from rest_framework import serializers

from .models import Launche


class LauncheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launche
        fields = "__all__"
