from django.urls import path
from .import views

urlpatterns = [
    path('enviar-mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('mostrar-mensajes/', views.mostrar_mensaje, name='mostrar_mensajes'),
    path('responder-mensaje/<int:id> ', views.responder_mensaje, name='responder_mensaje'),
]