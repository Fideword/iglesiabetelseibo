from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class Miembro(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Numero_Cedula = models.CharField(max_length=13)
    Numero_Celular = models.CharField(max_length=12,)
    Fecha_Nacimiento = models.DateField()
    Genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    Correo_Electronico = models.EmailField()
    Direccion_Residencia = models.CharField(max_length=50)
    Fecha_Conversion = models.DateField(null=True, blank=True)
    Fecha_Bautizo = models.DateField(null=True, blank=True)
    Estatus_Miembro = models.CharField(max_length=12, choices=[('Activo', 'Activo'), ('Descarriado', 'Descarriado')])
    Edades = models.ForeignKey('Edades', on_delete=models.SET_NULL, null=True)
    Ministerios = models.ManyToManyField('Ministerio', related_name='miembros')
    Sociedad = models.CharField(max_length=25, choices=[('Niños', 'Niños'), ('Jóvenes', 'Jóvenes'), ('Caballeros', 'Caballeros'), ('Damas', 'Damas')])
    Escuela_Dominical = models.ForeignKey('Escuela_Dominical', on_delete=models.SET_NULL, null=True)
    Imagen = models.ImageField(upload_to='miembros/imagenes')

    def __str__(self):
        return f"{self.Nombres} {self.Apellidos}"
    
class Servicio(models.Model):
    dia = models.CharField(max_length=50)
    hora = models.CharField(max_length=15)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/imagenes/',null=True)
    
    def __str__ (self):
        return self.dia

class Actividade(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='actividades/imagenes/', null=True)

    def __str__(self):
        return self.nombre
    
class Socie(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='sociedades/imagenes/', null=True)
    
    def __str__ (self):
        return self.nombre
    
class Minist(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='ministerios/imagenes/', null=True)
    
    def __str__ (self):
        return self.nombre

class Esc_Dom(models.Model):
    edades = models.CharField(max_length=10)
    maestro = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='escuela_dominical/imagenes/', null=True)
    
    def __str__ (self):
        return self.edades

class Edades(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Ministerio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Escuela_Dominical(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12, blank=True, null=True)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    
Group.objects.get_or_create(name='Administradores')
Group.objects.get_or_create(name='UsuariosNormales')
