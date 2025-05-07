from rest_framework import serializers
from ..models.passenger import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'passport_number', 'phone']