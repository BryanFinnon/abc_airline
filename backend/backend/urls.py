from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # redirige la racine vers votre API (optionnel)
    path('', RedirectView.as_view(url='/api/')),

    # interface d’administration Django
    path('admin/', admin.site.urls),

    # toutes les routes définies dans flights/urls.py
    path('api/', include('flights.urls')),
]
