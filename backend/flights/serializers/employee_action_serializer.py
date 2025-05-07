from rest_framework import serializers
from ..models.employee_action import EmployeeAction
from ..models.booking import Booking

class EmployeeActionSerializer(serializers.ModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking'
    )

    class Meta:
        model = EmployeeAction
        fields = ['id', 'booking_id', 'employee_name', 'action_type', 'timestamp']
        read_only_fields = ['id', 'timestamp']
