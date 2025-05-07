from rest_framework import viewsets
from ..models.luggage import Luggage
from ..serializers.luggage_serializer import LuggageSerializer

class LuggageViewSet(viewsets.ModelViewSet):
    queryset = Luggage.objects.select_related('booking').all()
    serializer_class = LuggageSerializer