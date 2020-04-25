from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from voyages.models import Marker, Line
from voyages.serializers import MarkerSerializer, LineSerializer


class MarkerList(ListAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    permission_classes = ()


class LineList(ListAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = ()
