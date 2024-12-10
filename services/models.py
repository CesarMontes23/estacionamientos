from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='services/')  # Necesitarás configurar media para esto
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']  # Ordenar por fecha de actualización descendente

    def __str__(self):
        return self.title
