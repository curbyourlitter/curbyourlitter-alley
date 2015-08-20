from rest_framework import viewsets

from .models import CanRequest
from .serializers import CanRequestSerializer


class CanRequestViewSet(viewsets.ModelViewSet):
    queryset = CanRequest.objects.all()
    serializer_class = CanRequestSerializer
