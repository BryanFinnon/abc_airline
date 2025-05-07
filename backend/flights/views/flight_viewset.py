from rest_framework import viewsets
from ..models.flight import Flight
from ..serializers.flight_serializer import FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related('route').all()
    serializer_class = FlightSerializer