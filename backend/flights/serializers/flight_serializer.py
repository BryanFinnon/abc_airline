from rest_framework import serializers
from ..models.flight import Flight
from ..models.route import Route 
from .route_serializer import RouteSerializer

class FlightSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    route_id = serializers.PrimaryKeyRelatedField(
        queryset=Route.objects.all(), source='route', write_only=True
    )

    class Meta:
        model = Flight
        fields = ['id', 'route', 'route_id', 'date', 'departure_time', 'arrival_time']
