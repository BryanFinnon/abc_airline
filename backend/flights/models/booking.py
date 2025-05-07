import uuid
from django.db import models
from .passenger import Passenger
from .flight import Flight
from .travel_class import TravelClass

class Booking(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('AMENDED', 'Amended'),
    ]

    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    travel_class = models.ForeignKey(TravelClass, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CONFIRMED')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.booking_id} ({self.passenger})"