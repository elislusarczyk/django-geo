from rest_framework import serializers
from .models import Airport


class AirportSerializer(serializers.ModelSerializer):
    distance = serializers.CharField(read_only=True)
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    def get_latitude(self, obj):
        return obj.point.y

    def get_longitude(self, obj):
        return obj.point.x

    class Meta:
        model = Airport
        fields = ('id', 'name', 'icao', 'point', 'distance', 'latitude', 'longitude')

