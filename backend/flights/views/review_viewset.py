from rest_framework import viewsets
from ..models.review import Review
from ..serializers.review_serializer import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('booking').all()
    serializer_class = ReviewSerializer