from django.contrib import admin
from .models import Pelicula, Serie, Stream

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Stream)
