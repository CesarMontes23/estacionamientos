# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estacionamiento  # Asegúrate de tener el modelo Estacionamiento
from django.http import JsonResponse

# Vista para la página principal
def home(request):
    # Aquí puedes agregar la lógica de la vista que quieras.
    data = {
        "message": "Bienvenido a la pagina principal"
    }
    return JsonResponse(data)

# Vista para mostrar todos los estacionamientos
def estacionamientos(request):
    estacionamientos_list = Estacionamiento.objects.all()  # Obtiene todos los estacionamientos
    data = {
        "estacionamientos": [
            {
                "nombre": estacionamiento.nombre,
                "tipo": estacionamiento.tipo,
                "ubicacion": estacionamiento.ubicacion,
                "contacto": estacionamiento.contacto,
                "capacidad_total": estacionamiento.capacidad_total,
                "capacidad_disponible": estacionamiento.capacidad_disponible,
            }
            for estacionamiento in estacionamientos_list
        ]
    }
    return JsonResponse(data)

# Vista para crear un nuevo estacionamiento
def crear_estacionamiento(request):
    if request.method == 'POST':
        # Crea un nuevo estacionamiento directamente usando el modelo
        nuevo_estacionamiento = Estacionamiento(
            nombre=request.POST.get('nombre'),
            ubicacion=request.POST.get('ubicacion'),
            capacidad=request.POST.get('capacidad'),
            # Agrega otros campos según el modelo
        )
        nuevo_estacionamiento.save()  # Guarda el nuevo estacionamiento
        return redirect('estacionamientos')  # Redirige a la lista de estacionamientos

    return render(request, 'estacionamientos/crear_estacionamiento.html')

# Vista para mostrar los detalles de un estacionamiento específico
def detalle_estacionamiento(request, pk):
    estacionamiento = Estacionamiento.objects.get(pk=pk)  # Obtén el estacionamiento por su ID
    return render(request, 'estacionamientos/detalle_estacionamiento.html', {'estacionamiento': estacionamiento})

# Vista para eliminar un estacionamiento
def eliminar_estacionamiento(request, pk):
    estacionamiento = Estacionamiento.objects.get(pk=pk)  # Obtén el estacionamiento por su ID
    if request.method == 'POST':
        estacionamiento.delete()  # Elimina el estacionamiento
        return redirect('estacionamientos')  # Redirige a la lista de estacionamientos

    return render(request, 'estacionamientos/eliminar_estacionamiento.html', {'estacionamiento': estacionamiento})
