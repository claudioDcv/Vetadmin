from rest_framework import serializers
from apps.core.models import Color


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'natural_key',)
