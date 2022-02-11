from datetime import timezone
from email.policy import default
from django.db import models
from AppSinLuz.forms import User
from django.db.models import ForeignKey, CASCADE, ImageField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Usuario(models.Model):
    username = models.CharField(max_length=50, default='')
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Usuario: {self.username} - Email: {self.email} - Dirección: {self.direccion} - Departamento: {self.departamento}"

class Administrativo(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Usuario: {self.username} - Email: {self.email}"

class Avatar(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 90, blank = False, null = False, default='')
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripción', max_length = 110, blank = False, null = False, default='')
    contenido = RichTextField(max_length = 140)
    imagen = ImageField(default='')
    imagen_user = ImageField(default='')
    autor = models.CharField('Autor',max_length = 90, default='')
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True, null= True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url

    def imagen_user_url(self):
        if self.imagen_user and hasattr(self.imagen_user, 'url'):
            return self.imagen_user.url
        

class Reclamo(models.Model):
    usuario = models.CharField(max_length=100)
    avatar = ImageField()
    identificacion = models.IntegerField()
    problema = models.CharField(max_length=30)
    fecha = models.DateField()
    resumen = models.CharField(max_length=50)
    detalles = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Usuario: {self.usuario} - Avatar: {self.avatar} - Problema: {self.problema} - Fecha: {self.fecha} - Resumen: {self.resumen} - Detalles: {self.detalles}"