from rest_framework import serializers
from ..models.booking import Booking
from ..models.passenger import Passenger
from ..models.flight import Flight
from ..models.travel_class import TravelClass
from .passenger_serializer import PassengerSerializer
from .flight_serializer import FlightSerializer
from .travel_class_serializer import TravelClassSerializer

class BookingSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    passenger_id = serializers.PrimaryKeyRelatedField(
        queryset=Passenger.objects.all(), source='passenger', write_only=True
    )
    flight = FlightSerializer(read_only=True)
    flight_id = serializers.PrimaryKeyRelatedField(
        queryset=Flight.objects.all(), source='flight', write_only=True
    )
    travel_class = TravelClassSerializer(read_only=True)
    travel_class_id = serializers.PrimaryKeyRelatedField(
        queryset=TravelClass.objects.all(), source='travel_class', write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id', 'booking_id', 'passenger', 'passenger_id',
            'flight', 'flight_id', 'travel_class', 'travel_class_id',
            'date_booked', 'status', 'total_price'
        ]
        read_only_fields = ['id', 'booking_id', 'date_booked']