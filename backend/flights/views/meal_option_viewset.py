from rest_framework import viewsets
from ..models.meal_option import MealOption
from ..serializers.meal_option_serializer import MealOptionSerializer

class MealOptionViewSet(viewsets.ModelViewSet):
    queryset = MealOption.objects.all()
    serializer_class = MealOptionSerializer