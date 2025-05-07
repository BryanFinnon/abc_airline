from rest_framework import viewsets
from ..models.travel_class import TravelClass
from ..serializers.travel_class_serializer import TravelClassSerializer

class TravelClassViewSet(viewsets.ModelViewSet):
    queryset = TravelClass.objects.all()
    serializer_class = TravelClassSerializer