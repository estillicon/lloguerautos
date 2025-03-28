from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar `include` también
from lloguer import views  # Importa las vistas desde la app 'lloguer'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', views.lista_automoviles, name='autos_lista'),  # Aquí está la vista para la lista de automóviles
]
