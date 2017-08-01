from apps.core.models import Color
from .serializers import ColorSerializer
from rest_framework import viewsets


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
