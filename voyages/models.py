from django.db import models


class Voyage(models.Model):
    name = models.CharField(max_length=255)


class Point(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()
