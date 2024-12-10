# estacionamientos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('estacionamientos/', views.estacionamientos, name='estacionamientos'),
]