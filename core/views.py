from django.shortcuts import render, redirect
from .models import Producto, Instalacion, Servicio
from .forms import ContactoForm


def home(request):
    productos_destacados = Producto.objects.filter(destacado=True, activo=True)
    servicios = Servicio.objects.filter(activo=True)

    return render(request, 'core/home.html', {
        'productos': productos_destacados,
        'servicios': servicios
    })


def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    instalaciones = Instalacion.objects.filter(visible=True)

    return render(request, 'core/catalogo.html', {
        'productos': productos,
        'instalaciones': instalaciones
    })

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contacto.html', {
                'form': ContactoForm(),
                'success': True
            })
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form})
