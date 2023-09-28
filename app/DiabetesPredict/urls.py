from django.urls import path
from .views import (PacientesAPIView,
                    ExameAPIView,
                    PacienteAPIView,
                    ExameFeedbackAPIView,
                    ExamesListaFeedbackAPIView
                    )





urlpatterns =[   
    path('pacientes/',PacientesAPIView.as_view(),name='pacientes'),
    path('pacientes/<str:cpf>/exames',PacienteAPIView.as_view(),name='paciente_exames'),
    path('exames/',ExameAPIView.as_view(),name='exames'),
    path('exames/<uuid:pk>/feedback',ExameFeedbackAPIView.as_view() , name='exame-feedback'),
    path('exames/lista/feedback',ExamesListaFeedbackAPIView.as_view() , name='exame-feedback'), 
]