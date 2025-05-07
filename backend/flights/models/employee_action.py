from django.db import models
from .booking import Booking

class EmployeeAction(models.Model):
    ACTION_CHOICES = [
        ('MODIFY', 'Modify'),
        ('CANCEL', 'Cancel'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='employee_actions')
    employee_name = models.CharField(max_length=100)
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_name} {self.action_type} on {self.booking}"