from .models import Airport
from airports.serializers import AirportSerializer
from rest_framework import generics
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry


class AirportList(generics.ListAPIView):
    serializer_class = AirportSerializer

    def get_queryset(self):
        query_point = self.request.query_params.get('point')
        radius = self.request.query_params.get('radius', 1000)
        
        if query_point is None:
            return Airport.objects.all()
            
        query_point = query_point.split(',')
        query_point = GEOSGeometry(f'POINT({query_point[0]} {query_point[1]})', srid=4326)

        queryset = Airport.objects.filter(
          point__distance_lte=(query_point, D(m=int(radius)))
        ).annotate(
          distance=Distance('point', query_point)
        ).order_by('distance')

        return queryset
