from rest_framework import viewsets
from ..models.employee_action import EmployeeAction
from ..serializers.employee_action_serializer import EmployeeActionSerializer

class EmployeeActionViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAction.objects.select_related('booking').all()
    serializer_class = EmployeeActionSerializer