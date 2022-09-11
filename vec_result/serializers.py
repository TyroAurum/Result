from rest_framework.serializers import ModelSerializer, Serializer
from .models import PinkIT


class PinkITSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super(
            PinkITSerializer, self).to_representation(instance)
        representation['DOB'] = instance.DOB.strftime('%d-%m-%Y')
        return representation

    class Meta:
        model = PinkIT
        fields = '__all__'
