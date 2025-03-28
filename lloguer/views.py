
from django.shortcuts import render
from .models import Automobil

def lista_automoviles(request):
    # Obtener todos los automóviles de la base de datos
    autos = Automobil.objects.all()
    return render(request, 'lloguer/autos_lista.html', {'autos': autos})

