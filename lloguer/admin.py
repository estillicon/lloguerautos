from django.contrib import admin

from .models import Automobil


class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')  # Mostrar estos campos en la lista
    search_fields = ('marca', 'model', 'matricula')  # Agregar búsqueda


admin.site.register(Automobil, AutomobilAdmin)
