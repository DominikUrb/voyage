from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from voyages.models import Point
from voyages.serializers import PointSerializer


class PointList(ListAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = ()
