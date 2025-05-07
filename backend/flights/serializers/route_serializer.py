from rest_framework import serializers
from ..models.route import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'departure', 'arrival']
