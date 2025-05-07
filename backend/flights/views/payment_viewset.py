from rest_framework import viewsets
from ..models.payment import Payment
from ..serializers.payment_serializer import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('booking').all()
    serializer_class = PaymentSerializer