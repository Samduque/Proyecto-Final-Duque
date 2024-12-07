from django.shortcuts import render
from django.shortcuts import redirect, render

from .forms import PeliculaFormulario, SerieFormulario, StreamFormulario

from .models import Stream, Pelicula, Serie

# Create your views here.

def inicio(request):
    return render(request, 'app_play/index.html')

def peliculas(request):
    
    query=request.GET.get('q')
    
    if query:
        pelis = Pelicula.objects.filter(titulo__icontains=query)
    else:
        pelis = Pelicula.objects.all()    
        
    return render(request,'app_play/peliculas.html', {"pelis": pelis, "query": query})

def series(request):
    
    query=request.GET.get('q')
    
    if query:
        series = Serie.objects.filter(titulo__icontains=query)
    else:
        series = Serie.objects.all()    
        
    return render(request,'app_play/series.html', {"series": series, "query": query})

def streaming(request):
    
    query=request.GET.get('q')
    
    if query:
        streaming = Stream.objects.filter(nombre__icontains=query)
    else:
        streaming = Stream.objects.all()    
        
    return render(request,'app_play/stream.html', {"streaming": streaming, "query": query})

def formulario_pelicula_api(request):
    
    if request.method == 'POST':
        formulario_pelicula_html = PeliculaFormulario(request.POST)
        
        if formulario_pelicula_html.is_valid():
            informacion_limpia = formulario_pelicula_html.cleaned_data
            pelicula = Pelicula( titulo=informacion_limpia['titulo'], 
                director=informacion_limpia['director'], 
                genero=informacion_limpia['genero'], 
                año=informacion_limpia['año'], 
                vistas=informacion_limpia['vistas'], 
                stream=informacion_limpia['stream'])
            pelicula.save()
            return redirect("peliculas")
        
    else:
        formulario_pelicula_html = PeliculaFormulario()
        
    return render(request,"app_play/forms/pelicula-formulario.html",{"formulario_pelicula_html": formulario_pelicula_html})    
        
        
def formulario_serie_api(request):
    
    if request.method == 'POST':
        formulario_serie_html = SerieFormulario(request.POST)
        
        if formulario_serie_html.is_valid():
            informacion_limpia = formulario_serie_html.cleaned_data
            serie = Serie( titulo=informacion_limpia['titulo'], 
                genero=informacion_limpia['genero'], 
                temporadas=informacion_limpia['temporadas'],
                vistas=informacion_limpia['vistas'], 
                stream=informacion_limpia['stream'])
            serie.save()
            return redirect("series")
        
    else:
        formulario_serie_html = SerieFormulario()
        
    return render(request,"app_play/forms/serie-formulario.html",{"formulario_serie_html": formulario_serie_html})    
                
                
def formulario_stream_api(request):
    
    if request.method == 'POST':
        formulario_stream_html = StreamFormulario(request.POST)
        
        if formulario_stream_html.is_valid():
            informacion_limpia = formulario_stream_html.cleaned_data
            stream = Stream( nombre=informacion_limpia['nombre'], 
                url=informacion_limpia['url'])
            stream.save()
            return redirect("stream")
        
    else:
        formulario_stream_html = StreamFormulario()
        
    return render(request,"app_play/forms/stream-formulario.html",{"formulario_stream_html": formulario_stream_html})
                