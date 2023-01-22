from django.db import models
from django.contrib.gis.db import models as geomodels


class Airport(geomodels.Model):
    name = models.CharField(max_length=100)
    icao = models.CharField(max_length=4)
    point = geomodels.PointField(
        srid=4326,
        geography=True,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Airport(name={self.name}, icao={self.icao}, point={self.point})"
