from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Genera 4 automóviles, 8 usuarios y asigna entre 1 y 2 reservas aleatorias'

    def handle(self, *args, **kwargs):
        fake = Faker()

       
        self.stdout.write(self.style.SUCCESS("Creando automóviles..."))
        for _ in range(4):
            marca = fake.company()
            model = fake.word()
            matricula = fake.bothify(text='??###??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Matricula aleatoria
            Automobil.objects.create(marca=marca, model=model, matricula=matricula)
        
        self.stdout.write(self.style.SUCCESS("Automóviles creados con éxito."))

       
        self.stdout.write(self.style.SUCCESS("Creando usuarios..."))
        for _ in range(8):
            nombre = fake.name()
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            user = User.objects.create_user(username=username, email=email, password=password)

     
            num_reservas = random.randint(1, 2)  

            for _ in range(num_reservas):
                automovil = random.choice(Automobil.objects.all())
                fecha_inicio = fake.date_this_year()  
                fecha_fin = fecha_inicio + timedelta(days=random.randint(1, 7))  

               
                Reserva.objects.get_or_create(
                    automovil=automovil,
                    usuario=user,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin
                )

        self.stdout.write(self.style.SUCCESS("Usuarios y reservas creados con éxito."))
