from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ..models import Curso
from ..serializers import CursoSerializer   

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