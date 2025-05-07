from rest_framework import viewsets
from ..models.passenger import Passenger
from ..serializers.passenger_serializer import PassengerSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer