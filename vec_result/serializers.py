from dataclasses import fields
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
from .models import PinkIT


class PinkITSerializer(ModelSerializer):

    class Meta:
        model = PinkIT
        fields = '__all__'
