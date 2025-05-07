from rest_framework import serializers
from ..models.review import Review
from ..models.booking import Booking

class ReviewSerializer(serializers.ModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking'
    )

    class Meta:
        model = Review
        fields = ['id', 'booking_id', 'rating', 'comments', 'date']
        read_only_fields = ['id', 'date']
