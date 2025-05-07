from django.db import models
from .booking import Booking
from .meal_option import MealOption

class MealSelection(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='meal_selections')
    meal_option = models.ForeignKey(MealOption, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.meal_option} for {self.booking}"