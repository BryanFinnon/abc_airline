from rest_framework import serializers
from ..models.meal_selection import MealSelection
from ..models.booking import Booking
from ..models.meal_option import MealOption
from .meal_option_serializer import MealOptionSerializer

class MealSelectionSerializer(serializers.ModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking'
    )
    meal_option = MealOptionSerializer(read_only=True)
    meal_option_id = serializers.PrimaryKeyRelatedField(
        queryset=MealOption.objects.all(), source='meal_option'
    )

    class Meta:
        model = MealSelection
        fields = ['id', 'booking_id', 'meal_option', 'meal_option_id', 'quantity']