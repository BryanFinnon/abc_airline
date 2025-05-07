from rest_framework import viewsets
from ..models.booking import Booking
from ..serializers.booking_serializer import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related('passenger', 'flight', 'travel_class').all()
    serializer_class = BookingSerializer