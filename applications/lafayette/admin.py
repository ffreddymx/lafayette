from django.contrib import admin
from .models import Amigo,Contacto,Operacion,Producto
# Register your models here.

admin.site.register(Amigo)
admin.site.register(Contacto)
admin.site.register(Operacion)
admin.site.register(Producto)