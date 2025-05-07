from rest_framework import viewsets
from ..models.route import Route
from ..serializers.route_serializer import RouteSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer