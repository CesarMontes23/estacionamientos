from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('estacionamientos/', views.estacionamientos, name='estacionamientos'),
]
