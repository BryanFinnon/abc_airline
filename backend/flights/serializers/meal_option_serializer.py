from rest_framework import serializers
from ..models.meal_option import MealOption

class MealOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealOption
        fields = ['id', 'name', 'price']