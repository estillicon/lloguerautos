from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.marca} {self.model} - {self.matricula}"

class Reserva(models.Model):
    automovil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        unique_together = ('automovil', 'fecha_inicio')  # Llave única

    def __str__(self):
        return f"Reserva de {self.automovil} por {self.usuario.username} del {self.fecha_inicio} al {self.fecha_fin}"
