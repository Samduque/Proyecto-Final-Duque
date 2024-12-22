from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    puntuacion = models.FloatField(default=0.0)
    duracion = models.CharField(max_length=50, blank=True, null=True, help_text="Duración en horas y minutos")
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    estreno = models.DateField()
    portada = models.ImageField(upload_to='portadas/', default='portadas/default_portada.jpg')
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    sinopsis = models.TextField(blank=True, null=True) 
    
    def __str__(self):
        return f"Titulo: {self.titulo},Puntuacion: {self.puntuacion}, Director: {self.director}, Duracion: {self.duracion} , Genero: {self.genero},Estreno en Argentina: {self.estreno}, Stream: {self.stream}"

class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    puntuacion = models.FloatField(default=0.0)
    genero = models.CharField(max_length=100)
    temporadas = models.IntegerField()
    portada = models.ImageField(upload_to='portadas/', default='portadas/default_portada.jpg')
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    sinopsis = models.TextField(blank=True, null=True) 
    
    def __str__(self):
        return f"Titulo: {self.titulo}, Puntuacion: {self.puntuacion},Genero: {self.genero}, Temporadas: {self.temporadas}, Stream: {self.stream},"

class Stream(models.Model):
    nombre = models.CharField(max_length=100)
    portada = models.ImageField(upload_to='portadas/', default='portadas/default_portada.jpg')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)   
    url = models.URLField(max_length=100)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, URL: {self.url}"
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images', blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    