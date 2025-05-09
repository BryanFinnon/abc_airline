from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from flights.views.booking_viewset import BookingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
urlpatterns = [
    # redirige la racine vers votre API (optionnel)
    path('', RedirectView.as_view(url='/api/')),

    # interface d’administration Django
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    # toutes les routes définies dans flights/urls.py
    path('api/', include('flights.urls')),
]
