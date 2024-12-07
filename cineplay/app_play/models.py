from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    año = models.IntegerField()
    vistas = models.IntegerField()
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Titulo: {self.titulo}, Director: {self.director}, Genero: {self.genero},Año: {self.año}, Stream: {self.stream}"

class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    temporadas = models.IntegerField()
    vistas = models.IntegerField()
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Titulo: {self.titulo}, Genero: {self.genero}, Temporadas: {self.temporadas}, Stream: {self.stream}"

class Stream(models.Model):
    nombre = models.CharField(max_length=100)   
    url = models.URLField(max_length=100)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, URL: {self.url}"