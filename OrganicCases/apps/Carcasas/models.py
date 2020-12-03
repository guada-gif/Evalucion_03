from django.db import models
from django.conf import settings

# Create your models here.


class Material(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    valor = models.IntegerField()
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.nombre


class ModeloEquipo(models.Model):
    nombre = models.CharField(max_length=70)
    valor = models.IntegerField()
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.nombre


class Carcasa(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=400)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(null=True, blank=True)
    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    terminada = models.BooleanField(default=False)
    material = models.ForeignKey(
        Material, related_name='carcasas', on_delete=models.CASCADE, null=True)
    modeloEquipo = models.ForeignKey(
        ModeloEquipo, related_name='carcasas', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre + " por " + self.creador.username

    def save(self, *args, **kwargs):
        # Calculamos en base al valor del material y del equipo, el precio de la carcasa
        precio_material = 0
        if self.material:
            precio_material = self.material.valor

        precio_modelo = 0
        if self.modeloEquipo:
            precio_modelo = self.modeloEquipo.valor

        self.precio = precio_material + precio_modelo

        # Porcentaje de ganancias
        if self.precio > 0:
            self.precio = self.precio * 1.3
        super(Carcasa, self).save(*args, **kwargs)
