from django.contrib import admin
from .models import Project
# Register your models here.
# Necesario para ver los campos ocultos de created y updated.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)