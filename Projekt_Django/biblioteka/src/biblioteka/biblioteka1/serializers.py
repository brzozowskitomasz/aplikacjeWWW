from rest_framework import serializers
from django.db import models

class biblioteka2(serializers.Serializer):
    nazwa = models.CharField(max_length=45)

    def validate_title(self, value):
        """
        cos
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError(
                "blad",
            )
        return value


