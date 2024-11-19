from django.contrib import admin
from .models import Clasificacion, Posteo

# Register your models here.

class ClasificacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PosteoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Clasificacion,ClasificacionAdmin)
admin.site.register(Posteo,PosteoAdmin)
