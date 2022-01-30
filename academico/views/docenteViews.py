from ..models import Docente
from ..serializers import DocenteSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

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
    