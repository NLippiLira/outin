from django.contrib import admin

# Register your models here.
from .models import Producto, Servicio, Instalacion, Contacto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio', 'incluye_instalacion', 'destacado', 'activo')
    list_filter = ('tipo', 'destacado', 'activo')
    search_fields = ('nombre',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')

@admin.register(Instalacion)
class InstalacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'visible')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'creado', 'atendido')
    list_filter = ('atendido',)
    