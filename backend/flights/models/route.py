from django.db import models

class Route(models.Model):
    departure = models.CharField(max_length=100)
    arrival   = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.departure} → {self.arrival}"
