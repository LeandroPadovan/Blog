from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class usuario(models.Model):
    username=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    nacimiento=models.DateField()
    telefono=models.IntegerField()

    def __str__(self):
        return f"Usuario: {self.username} - Nombre: {self.nombre} - Apellido: {self.apellido} - Mail: {self.email}"



class post(models.Model):
    titulo=models.CharField(max_length=200)
    reseña=models.CharField(max_length=500)
    contenido=models.TextField(max_length=5000)
    imagen=models.ImageField(upload_to="imgpost", null=True, blank=True)
    fecha= models.DateField()
    autor= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Titulo: {self.titulo} - Reseña: {self.reseña} - Fecha: {self.fecha}"

class avatar(models.Model):
    imagen= models.ImageField(upload_to="avatar")
    user= models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Imagen: {self.imagen}"