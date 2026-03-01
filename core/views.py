import requests
from django.conf import settings
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
    success = False

    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():
            contacto = form.save()

            # Construir mensaje
            subject = "Nuevo mensaje desde OUT-IN"
            body = f"""
            Nombre: {contacto.nombre}
            Teléfono: {contacto.telefono}
            Email: {contacto.email}

            Mensaje:
            {contacto.mensaje}
            """

            # Enviar usando Resend API
            response = requests.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "from": settings.EMAIL_FROM,
                    "to": settings.EMAIL_TO,
                    "subject": subject,
                    "text": body,
                },
            )

            if response.status_code == 200:
                success = True

    else:
        form = ContactoForm()

    return render(request, "core/contacto.html", {
        "form": form,
        "success": success
    })