from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from voyages.models import Voyage, Marker, Line


class MarkerSerializer(ModelSerializer):
    position = SerializerMethodField()

    class Meta:
        model = Marker
        fields = ('id', 'position', 'voyage')

    def get_position(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}


class LineSerializer(ModelSerializer):
    path = SerializerMethodField()

    class Meta:
        model = Line
        fields = ('id', 'path', 'voyage')

    def get_path(self, obj):
        return {'lat': obj.lat1, 'lng': obj.lng1}, {'lat': obj.lat2, 'lng': obj.lng2}


class VoyageSerializer(ModelSerializer):

    class Meta:
        model = Voyage
        fields = '__all__'
