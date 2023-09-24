from django.urls import path
from .views import (PacienteApiView,ExameApiView)

urlpatterns =[
    path('pacientes',PacienteApiView.as_view(),name='pacientes'),
    path('exames',ExameApiView.as_view(),name='exames'),
]