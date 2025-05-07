from django.db import models
from .flight import Flight
from .travel_class import TravelClass

class Price(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='prices')
    travel_class = models.ForeignKey(TravelClass, on_delete=models.CASCADE, related_name='prices')
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ('flight', 'travel_class')

    def __str__(self):
        return f"{self.travel_class} - {self.amount}"