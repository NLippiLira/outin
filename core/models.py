from django.db import models

# Create your models here.

class Producto(models.Model):

    TIPO_CHOICES = [
        ('PTZ', 'PTZ'),
        ('FIJA', 'Fija'),
        ('SOLAR', 'Fotovoltaica'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    incluye_instalacion = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='productos/')
    destacado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(
        max_length=50,
        help_text="Ej: bi-tools, bi-shield-check"
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Instalacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='instalaciones/')
    fecha = models.DateField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"
