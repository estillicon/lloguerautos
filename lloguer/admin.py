

from django.contrib import admin
from .models import Automobil, Reserva

@admin.register(Automobil)
class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automovil', 'usuario', 'fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_inicio', 'fecha_fin', 'automovil')
    search_fields = ('automovil__marca', 'automovil__model', 'usuario__username')


