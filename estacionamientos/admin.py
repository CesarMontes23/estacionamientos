from django.contrib import admin
from .models import Estacionamiento

class EstacionamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'ubicacion', 'contacto', 'capacidad_total', 'capacidad_disponible')

admin.site.register(Estacionamiento, EstacionamientoAdmin)
