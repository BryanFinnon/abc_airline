from rest_framework import serializers
from ..models.pickup_drop_service import PickupDropService
from ..models.booking import Booking

class PickupDropServiceSerializer(serializers.ModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking'
    )

    class Meta:
        model = PickupDropService
        fields = ['id', 'booking_id', 'service_type', 'address', 'cost']