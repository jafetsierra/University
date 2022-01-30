from django.urls import path
from  .views import *

urlpatterns = [
    path('docente/create',DocenteCreateView.as_view(),name='docente_create'),
    path('docente/list',DocenteListView.as_view(),name='docente_list'),
    path('docente/detail/<int:pk>',DocenteDetailView.as_view(),name='docente_detail'),
    path('docente/update/<int:pk>',DocenteUpdateView.as_view(),name='docente_update'),
    path('docente/delete/<int:pk>',DocenteDeleteView.as_view(),name='docente_delete'),
    path('curso/create',CursoCreateView.as_view(),name='curso_create'),
    path('curso/list',CursoListView.as_view(),name='curso_list'),
    path('curso/detail/<int:docente_id>',CursoDetailView.as_view(),name='curso_detail'),
    path('curso/update/<int:pk>',CursoUpdateView.as_view(),name='curso_update'),
    path('curso/delete/<int:pk>',CursoDeleteView.as_view(),name='curso_delete'),
    path('estudiante/create',EstudianteCreateView.as_view(),name='estudiante_create'),
    path('estudiante/list/<int:age>',EstudianteListView.as_view(),name='estudiante_list'),
]
