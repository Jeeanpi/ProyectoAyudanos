from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.

# Tabla CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    celular = models.CharField(max_length=10)
    direccion = models.TextField()
    region = models.CharField(max_length=15)
    comuna = models.CharField(max_length=15)
    idCliente = models.CharField(max_length=15)
    password = models.TextField(max_length=15)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

# Tabla MASCOTA
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    propietario = models.ForeignKey(Cliente, on_delete=CASCADE)
    sexo = models.CharField(max_length=10)
    raza = models.CharField(max_length=10)
    fechaNacimiento = models.DateField()
    numeroMicroChip = models.IntegerField()
    veterinaria = models.CharField(max_length=20)
    direccion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="mascotas", null = True)

    def __str__(self):
        return self.nombre

class ContratarPlan(models.Model):
    nombreCliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    nombreMascota = models.ForeignKey(Mascota, on_delete=CASCADE)
    tipoPlan = models.CharField(max_length=10)
    fechaContrato = models.DateField()

    def __str__(self):
        return self.tipoPlan
