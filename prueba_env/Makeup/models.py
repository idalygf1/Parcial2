from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=30) #CharField es igual a Varchar en BD
    descripcion=models.CharField(max_length=200)
    stock=models.IntegerField() #IntegerField es igual a tipo entero en BD
    precio=models.IntegerField()
    imagen=models.CharField(max_length=202,default=True)


    def __str__(self): #para que retorne los valores 
        return self.nombre

class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    apellido_p=models.CharField(max_length=20)
    apellido_m=models.CharField(max_length=20)
    email=models.EmailField()
    telefono=models.CharField(max_length=13)
    password=models.CharField(max_length=8,default=True)


    def __str__(self):
        return self.usuario









