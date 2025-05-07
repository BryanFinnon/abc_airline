from django.db import models
from .booking import Booking

class PickupDropService(models.Model):
    SERVICE_TYPE = [
        ('PICKUP', 'Pickup'),
        ('DROPOFF', 'Dropoff'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='pickup_services')
    service_type = models.CharField(max_length=8, choices=SERVICE_TYPE)
    address = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.service_type} for {self.booking}"