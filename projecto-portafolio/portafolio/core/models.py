from django.db import models

# Create your models here.
from tabnanny import verbose
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Clasificacion(models.Model):
    name=models.CharField(max_length=100,verbose_name="nombre")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
    
    def __str__(self):
        return self.name

class Posteo(models.Model):
    title=models.CharField(max_length=100,verbose_name="titulo")
    content=models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="posteos", null=True, blank=True,
        verbose_name="Imagen")
    published=models.DateTimeField(default=now,verbose_name="Fecha de Publicación")
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Autor")
    classification=models.ManyToManyField(Clasificacion,verbose_name="Categorias")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")


    class Meta:
        verbose_name="Posteo"
        verbose_name_plural="Posteos"
    
    def __str__(self):
        return self.title