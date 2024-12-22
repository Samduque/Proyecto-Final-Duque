from django.shortcuts import render
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .forms import PeliculaFormulario, PerfilDeUsuarioFormulario, SerieFormulario, StreamFormulario, UsuarioEditFormulario
from .models import Perfil, Stream, Pelicula, Serie

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
@login_required
def formulario_pelicula(request):
    
    if request.method == 'POST':
        form_pelicula = PeliculaFormulario(request.POST)
        
        if form_pelicula.is_valid():
            form_pelicula.save()
            return redirect("peliculas")
    else:
        form_pelicula = PeliculaFormulario()
        
    return render(request,"app_play/forms/pelicula-formulario.html",{"form": form_pelicula})    
@login_required
def eliminar_pelicula(request, id):
    
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect("peliculas")  
@login_required
def editar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    
    if request.method == 'POST':
        form = PeliculaFormulario(request.POST, request.FILES, instance=pelicula)  
        if form.is_valid():
            form.save()  
            return redirect('detalle_pelicula', id=pelicula.id) 
    else:
        form = PeliculaFormulario(instance=pelicula)

    return render(request, 'app_play/forms/pelicula-editar.html', {'edit': form})


def detalle_pelicula(request, id):
    
    pelicula = get_object_or_404(Pelicula, id=id)
    portada_url = pelicula.portada.url if pelicula.portada else 'portadas/default_portada.jpg'
    
    return render(request, 'app_play/detalle-pelicula.html', {'pelicula': pelicula, 'portada_url': portada_url})
@login_required
def formulario_serie(request):
    
    if request.method == 'POST':
        form_serie = SerieFormulario(request.POST)
        
        if form_serie.is_valid():
            form_serie.save()
            return redirect("series")
    else:
        form_serie = SerieFormulario()
        
    return render(request,"app_play/forms/serie-formulario.html",{"form": form_serie})     

@login_required
def eliminar_serie(request, id):
    
    serie = Serie.objects.get(id=id)
    serie.delete()
    return redirect("series")      
@login_required
def editar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    
    if request.method == 'POST':
        form = SerieFormulario(request.POST, request.FILES, instance=serie) 
        if form.is_valid():
            form.save()  
            return redirect('detalle_serie', id=serie.id) 
    else:
        form = SerieFormulario(instance=serie)

    return render(request, 'app_play/forms/serie-editar.html', {'edit': form})

def detalle_serie(request, id):
    
    serie = get_object_or_404(Serie, id=id)
    portada_url = serie.portada.url if serie.portada else 'portadas/default_portada.jpg'
    
    return render(request, 'app_play/detalle-serie.html', {'serie': serie, 'portada_url': portada_url})
@login_required              
def formulario_stream(request):
    
    if request.method == 'POST':
        form_stream = StreamFormulario(request.POST)
        
        if form_stream.is_valid():
            form_stream.save()
            return redirect("stream")
        
    else:
        form_stream = StreamFormulario()
        
    return render(request,"app_play/forms/stream-formulario.html",{"form": form_stream})

@login_required
def eliminar_stream(request, id):
    
    stream = Stream.objects.get(id=id)
    stream.delete()
    return redirect("stream")
@login_required
def editar_stream(request, id):
    
    stream = get_object_or_404(Stream, id=id)
    
    if request.method == 'POST':
        edit_stream = StreamFormulario(request.POST, request.FILES, instance=stream)
        
        if edit_stream.is_valid():
            edit_stream.save()
            return redirect("detalle_stream", id = stream.id)
    else:
        edit_stream = StreamFormulario(instance=stream)
        
    return render(request,"app_play/forms/stream-editar.html",{"edit": edit_stream})

def detalle_stream(request, id):
    
    stream = get_object_or_404(Stream, id=id)
    portada_url = stream.portada.url if stream.portada else 'portadas/default_portada.jpg'
    
    return render(request, 'app_play/detalle-stream.html', {'stream': stream,'portada_url': portada_url})

def top_5(request):
    top_peliculas = Pelicula.objects.all().order_by('-puntuacion')[:5]
    top_series = Serie.objects.all().order_by('-puntuacion')[:5]
    
    return render(request, 'app_play/top_5.html',{'top_peliculas': top_peliculas, 'top_series': top_series})                
                
def vista_inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido a CinePlay {request.user.username}!")
            return redirect('inicio')
        else:
            return render(request, 'app_play/forms/login.html')
    else:
        return render(request, 'app_play/forms/login.html')    
@login_required    
def vista_cerrar_sesion(request):        
    logout(request)
    messages.success(request, f"Hasta pronto!")
    return redirect('inicio_sesion')

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'app_play/forms/registro.html', {'form': form})            
@login_required
def mostrar_perfil(request):
    return render(request, 'app_play/perfil.html')
@login_required
def editar_perfil(request):
    
    usuario = request.user
    perfil, created = Perfil.objects.get_or_create(usuario=usuario)
    
    if request.method == 'POST':
        usuario_form = UsuarioEditFormulario(request.POST, instance = usuario)
        perfil_form = PerfilDeUsuarioFormulario(request.POST,request.FILES, instance = perfil) 
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            messages.success(request, f"Perfil actualizado con exito!")
            return redirect('perfil')
        else:
            messages.success(request, f"Hubo algún error al actualizar el perfil, por favor comprueba los datos.")
            return redirect('editar_perfil')
        
    else:
        usuario_form = UsuarioEditFormulario(instance = usuario)
        perfil_form = PerfilDeUsuarioFormulario(instance = perfil)
    return render(request, 'app_play/forms/editar-perfil.html', {'form': usuario_form, 'perfil_form': perfil_form})

@login_required
def cambiar_contraseña(request):
    
    usuario = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, usuario)
            return redirect('inicio_sesion')
        else:
            return redirect('inicio')
    else:
        form = PasswordChangeForm(usuario)
        
    return render(request, 'app_play/forms/cambiar-contraseña.html', {'form': form})

def sobre_nosotros(request):
    return render(request, 'app_play/sobre-nosotros.html')

