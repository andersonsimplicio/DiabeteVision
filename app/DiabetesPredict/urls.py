from django.urls import path
from .views import (PacientesAPIView,ExameAPIView,PacienteAPIView)

urlpatterns =[
    path('exames',ExameAPIView.as_view(),name='exames'),
    path('pacientes',PacientesAPIView.as_view(),name='pacientes'),
    path('pacientes/<str:cpf>/exames',PacienteAPIView.as_view(),name='paciente_exames   ')
]