from django.db import models


class Voyage(models.Model):
    name = models.CharField(max_length=255)


class Marker(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()


class Line(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    lat1 = models.FloatField()
    lng1 = models.FloatField()
    lat2 = models.FloatField()
    lng2 = models.FloatField()
