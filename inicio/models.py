from django.db import models

# Create your models here.

# class Producto(models.Model):
#     nombre = models.CharField(max_length=20)
#     descripcion = models.CharField(max_length=20)
#     cantidad = models.IntegerField()
    
    # def __str__(self):
    #     return f'Soy {self.nombre}, tengo {self.edad}'
    
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    legajo = models.IntegerField(default=00000)
    fecha_nacimiento = models.DateField()
    
