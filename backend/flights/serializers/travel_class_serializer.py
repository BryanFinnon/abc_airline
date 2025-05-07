from rest_framework import serializers
from ..models.travel_class import TravelClass

class TravelClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelClass
        fields = ['id', 'name']