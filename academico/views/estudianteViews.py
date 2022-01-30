from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import EstudianteSerializer
from ..models import Estudiante
from django.db.models import Q

#-------Estudiante views--------
class EstudianteCreateView(CreateAPIView):
    serializer_class = EstudianteSerializer

class EstudianteListView(ListAPIView):
    #queryset = Estudiante.objects.filter(Q(name='Maria') | ~Q(name='Danilo'))
    serializer_class = EstudianteSerializer
    def get_queryset(self):
        edad = self.kwargs['age']
        return Estudiante.objects.filter(age__gte=edad)