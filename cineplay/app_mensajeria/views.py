from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Mensaje
# Create your views here.
@login_required
def enviar_mensaje(request):
    
    if request.method == 'POST':
        asunto = request.POST.get('asunto')
        cuerpo = request.POST.get('cuerpo')
        destinatario = request.POST.get('destinatario')
        destinatario = User.objects.get(username=destinatario)
        mensaje = Mensaje.objects.create(remitente=request.user, asunto=asunto, cuerpo=cuerpo, destinatario=destinatario)
        mensaje.save()
        return redirect('mostrar_mensajes')
    
    usuarios = User.objects.exclude(username=request.user.username)   
    
    return render(request, 'app_mensajeria/enviar-mensaje.html',{"usuarios": usuarios})
@login_required
def mostrar_mensaje(request):
    
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_de_envio')
    
    return render(request, 'app_mensajeria/mostrar-mensajes.html', {"mensajes": mensajes})
@login_required
def responder_mensaje(request, id):
    mensaje_original = get_object_or_404(Mensaje, id=id)
    
    if request.method == 'POST':
        asunto = request.POST.get('asunto', f"Re: {mensaje_original.asunto}")
        cuerpo = request.POST.get('cuerpo', '').strip()
        destinatario_username = request.POST.get('destinatario')
        
        if not cuerpo:
            return render(request, 'app_mensajeria/responder-mensaje.html', {
                "mensaje": mensaje_original,
                "error": "El cuerpo del mensaje no puede estar vacío.",
            })
        
        try:
            destinatario = User.objects.get(username=destinatario_username)
        except User.DoesNotExist:
            return render(request, 'app_mensajeria/responder-mensaje.html', {
                "mensaje": mensaje_original,
                "error": "El destinatario no es válido.",
            })
        
        nuevo_mensaje = Mensaje.objects.create(
            remitente=request.user,
            asunto=asunto,
            cuerpo=cuerpo,
            destinatario=destinatario
        )
        nuevo_mensaje.save()
        return redirect('mostrar_mensajes')
    
    return render(request, 'app_mensajeria/responder-mensaje.html', {
        "mensaje": mensaje_original
    })