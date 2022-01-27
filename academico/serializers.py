from rest_framework import serializers
from .models import Curso, Docente, Estudiante

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Curso
        fields = ['id', 'name', 'credits', 'capacity', 'docente']
        

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Docente
        fields = [
            'id',
            'nombres',
            'sexo',
            'apellido_paterno',
            'apellido_materno',
        ]

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Estudiante
        fields = [
            'id',
            'name',
            'lastname',
            'age',
            'curso',
        ]