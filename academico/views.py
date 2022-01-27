from cgitb import lookup
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import CursoSerializer, DocenteSerializer, EstudianteSerializer
from .models import Curso, Docente, Estudiante
# Create your views here.

#--------Docente views--------
class DocenteCreateView(CreateAPIView):
    serializer_class = DocenteSerializer

class DocenteListView(ListAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    
class DocenteDetailView(RetrieveAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    
class DocenteUpdateView(UpdateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class DocenteDeleteView(DestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    
#--------Curso views--------
class CursoCreateView(CreateAPIView):
    serializer_class = CursoSerializer
    
class CursoListView(ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetailView(ListAPIView):
    serializer_class = CursoSerializer
    lookup_field = 'docente_id'
    def get_queryset(self):
        docenteId = self.kwargs['docente_id']
        return Curso.objects.filter(docente_id=docenteId)

class CursoUpdateView(UpdateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDeleteView(DestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#-------Estudiante views--------
class EstudianteCreateView(CreateAPIView):
    serializer_class = EstudianteSerializer

class EstudianteListView(ListAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer