from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, null=True, blank=True)

class Estacionamiento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    ubicacion = models.TextField()
    contacto = models.CharField(max_length=15)
    capacidad_total = models.IntegerField()
    capacidad_disponible = models.IntegerField()

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    fecha_hora_reserva = models.DateTimeField()
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.CharField(max_length=50)

class Transaccion(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_transaccion = models.DateTimeField()
    metodo_pago = models.CharField(max_length=50, null=True, blank=True)

# (Continúa definiendo las demás tablas como Opiniones, Sensores, etc.)
