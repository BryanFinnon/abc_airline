from rest_framework import viewsets
from ..models.pickup_drop_service import PickupDropService
from ..serializers.pickup_drop_service_serializer import PickupDropServiceSerializer

class PickupDropServiceViewSet(viewsets.ModelViewSet):
    queryset = PickupDropService.objects.select_related('booking').all()
    serializer_class = PickupDropServiceSerializer