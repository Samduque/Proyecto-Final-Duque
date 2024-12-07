from django import forms

from .models import Stream


class PeliculaFormulario(forms.Form):
    titulo = forms.CharField(label='Pelicula', max_length=100)
    director = forms.CharField(label='Director', max_length=100)
    genero = forms.CharField(label='Genero', max_length=100)
    año = forms.IntegerField(label='Año', min_value=1900)
    vistas = forms.IntegerField(label='Vistas', min_value=0)
    stream = forms.ModelChoiceField(queryset=Stream.objects.all(), label='Stream')
    
class SerieFormulario(forms.Form):
    titulo = forms.CharField(label='Serie', max_length=100)
    genero = forms.CharField(label='Genero', max_length=100)
    temporadas = forms.IntegerField(label='Temporadas', min_value=1)
    vistas = forms.IntegerField(label='Vistas', min_value=0)
    stream = forms.ModelChoiceField(queryset=Stream.objects.all(), label='Stream')    
    
    
class StreamFormulario(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    url = forms.URLField(label='Url', max_length=100)
    
    