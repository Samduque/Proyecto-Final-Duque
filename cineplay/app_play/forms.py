from django import forms
from django.contrib.auth.models import User

from .models import Perfil, Stream, Pelicula, Serie


class UsuarioEditFormulario(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class PerfilDeUsuarioFormulario(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ['photo']        

class PeliculaFormulario(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'puntuacion', 'duracion', 'genero', 'estreno', 'portada', 'stream', 'sinopsis']
        
    portada = forms.ImageField(required=False)     
    
    
class SerieFormulario(forms.ModelForm):
    
    class Meta:
        model = Serie
        fields = ['titulo', 'puntuacion', 'genero', 'temporadas', 'portada', 'stream', 'sinopsis']
    
class StreamFormulario(forms.ModelForm):
    
    class Meta:
        model = Stream
        fields = ['nombre', 'url','portada', 'precio']
    
    