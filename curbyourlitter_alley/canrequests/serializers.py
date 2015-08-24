from rest_framework import serializers

from .models import CanRequest


class CanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanRequest
