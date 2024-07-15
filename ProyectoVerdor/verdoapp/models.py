from django.db import models

# Create your models here.

class User(models.Model):
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    contraseña = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    rut = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

def __str__(self):
    return str(self.nombre)+" "+str(self.apellido_paterno)