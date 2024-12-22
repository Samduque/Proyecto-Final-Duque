from django.urls import path
from app_play import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('inicio-sesion/', views.vista_inicio_sesion, name='inicio_sesion'),
    path('cerrar-sesion/', views.vista_cerrar_sesion, name='cerrar_sesion'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('perfil/', views.mostrar_perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambiar-contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    
    path('peliculas/', views.peliculas, name='peliculas'), 
    path('pelicula-formulario/' , views.formulario_pelicula,name='pelicula_formulario'),
    path('eliminar-pelicula/<int:id>/' , views.eliminar_pelicula,name='eliminar_pelicula'),
    path('editar-pelicula/<int:id>/' , views.editar_pelicula,name='editar_pelicula'),
    path('detalle-pelicula/<int:id>/' , views.detalle_pelicula,name='detalle_pelicula'),
    
    path('series/', views.series, name='series'),
    path('serie-formulario/' , views.formulario_serie,name='serie_formulario'),
    path('eliminar-serie/<int:id>' , views.eliminar_serie,name='eliminar_serie'),
    path('editar-serie/<int:id>' , views.editar_serie,name='editar_serie'),
    path('detalle-serie/<int:id>/' , views.detalle_serie,name='detalle_serie'),
    
    path('stream/', views.streaming, name='stream'),
    path('stream-formulario/' , views.formulario_stream,name='stream_formulario'),
    path('eliminar-stream/<int:id>' , views.eliminar_stream,name='eliminar_stream'),
    path('editar-stream/<int:id>' , views.editar_stream,name='editar_stream'),
    path('detalle-stream/<int:id>/' , views.detalle_stream,name='detalle_stream'),
    
    path('top_5/', views.top_5,name='top_5'),
    
]