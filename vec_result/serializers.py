from dataclasses import fields
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
from .models import PinkIT
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    pinkits = PrimaryKeyRelatedField(many=True, queryset=PinkIT.objects.all())
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'pinkits', 'owner']


class PinkITSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super(
            PinkITSerializer, self).to_representation(instance)
        representation['DOB'] = instance.DOB.strftime('%d-%m-%Y')
        return representation

    class Meta:
        model = PinkIT
        fields = '__all__'
