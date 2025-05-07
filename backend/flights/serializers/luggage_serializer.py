from rest_framework import serializers
from ..models.luggage import Luggage
from ..models.booking import Booking

class LuggageSerializer(serializers.ModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking'
    )

    class Meta:
        model = Luggage
        fields = ['id', 'booking_id', 'luggage_id', 'weight', 'bag_count']
        read_only_fields = ['id', 'luggage_id']
