from rest_framework import viewsets
from ..models.price import Price
from ..serializers.price_serializer import PriceSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.select_related('flight', 'travel_class').all()
    serializer_class = PriceSerializer