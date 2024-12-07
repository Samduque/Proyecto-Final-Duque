from django.urls import path
from app_play import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('series/', views.series, name='series'),
    path('stream/', views.streaming, name='stream'),
    path('pelicula-formulario/' , views.formulario_pelicula_api,name='pelicula_formulario'),
    path('serie-formulario/' , views.formulario_serie_api,name='serie_formulario'),
    path('stream-formulario/' , views.formulario_stream_api,name='stream_formulario'),
]