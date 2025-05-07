from rest_framework import viewsets
from ..models.meal_selection import MealSelection
from ..serializers.meal_selection_serializer import MealSelectionSerializer

class MealSelectionViewSet(viewsets.ModelViewSet):
    queryset = MealSelection.objects.select_related('booking', 'meal_option').all()
    serializer_class = MealSelectionSerializer