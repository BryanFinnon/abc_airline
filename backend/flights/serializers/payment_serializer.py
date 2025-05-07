from rest_framework import serializers
from ..models.payment import Payment
from ..models.booking import Booking

class PaymentSerializer(serializers.ModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking'
    )

    class Meta:
        model = Payment
        fields = ['id', 'booking_id', 'transaction_id', 'card_number', 'amount', 'date']
        read_only_fields = ['id', 'transaction_id', 'date']