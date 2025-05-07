from rest_framework import serializers
from ..models.price import Price
from ..models.flight import Flight
from ..models.travel_class import TravelClass
from .flight_serializer import FlightSerializer
from .travel_class_serializer import TravelClassSerializer

class PriceSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)
    flight_id = serializers.PrimaryKeyRelatedField(
        queryset=Flight.objects.all(), source='flight', write_only=True
    )
    travel_class = TravelClassSerializer(read_only=True)
    travel_class_id = serializers.PrimaryKeyRelatedField(
        queryset=TravelClass.objects.all(), source='travel_class', write_only=True
    )

    class Meta:
        model = Price
        fields = ['id', 'flight', 'flight_id', 'travel_class', 'travel_class_id', 'amount'] 