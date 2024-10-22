from django.db import models

# Create your models here.
# Modelo para formacion = Course
class Course (models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    degree_title = models.CharField(max_length=300, verbose_name='Titulo Obtenido')
    description = models.TextField(verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha modificacion')
    # sub clase para cambiarle el nombre a espanol en la pagina admin con ordenanza
    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'
        ordering = ['created']
    #simplemente retorna la variable titulo para que tenga el titulo dado el nombre por el proyecto.
    def __str__(self):
        return self.title



#Modelo para conocimientos = skills
class Skill(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    image = models.ImageField(upload_to='projects',verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha modificacion')
    # sub clase para cambiarle el nombre a espanol en la pagina admin con ordenanza
    class Meta:
        verbose_name = 'Conocimiento'
        verbose_name_plural = 'Conocimientos'
        ordering = ['created']
    #simplemente retorna la variable titulo para que tenga el titulo dado el nombre por el proyecto.
    def __str__(self):
        return self.title
