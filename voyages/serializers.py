from rest_framework.serializers import ModelSerializer, Serializer

from voyages.models import Point, Voyage


class PointSerializer(ModelSerializer):

    class Meta:
        model = Point
        fields = '__all__'


class VoyageSerializer(ModelSerializer):

    class Meta:
        model = Voyage
        fields = '__all__'
