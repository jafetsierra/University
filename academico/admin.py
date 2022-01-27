from django.contrib import admin
from .models import Curso, Docente, Estudiante
# Register your models here.

#First way to register a model in admin
#admin.site.register(Curso)

#A second way to do the same thing
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    #list_display        = ('id','name','credits')
    #search_fields       = ('name','credits')
    #list_editable       = ('name','credits')
    #list_display_links  = ('name',)
    #list_filter         = ('credits',)
    list_per_page        = 10
    #exclude             = ('credits',)
    
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_per_page        = 10
    search_fields        = ('nombres','apellido_paterno','apellido_materno')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_per_page        = 10
    search_fields        = ('name','lastname')
    list_filter          = ('name','lastname')
    #list_display_links   = ('name','lastname')
    #list_display         = ('name','lastname','age')