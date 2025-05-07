import uuid
from django.db import models
from .booking import Booking

class Luggage(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='luggages')
    luggage_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bag_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Luggage {self.luggage_id} ({self.weight}kg)"