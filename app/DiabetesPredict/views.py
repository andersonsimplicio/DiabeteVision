from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework  import status

from .models import (
    Paciente,
    Exame,
    ConsultaFeedBack
)

from .serialize import (
    PacientesSerial,
    PacienteSerial,
    PacienteListaExamesSerial,
    ExameSerial,
    ExamesSerial,
    ConsultaFeedBackSerial
)

class PacientesAPIView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacientesSerial


class PacienteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PacienteListaExamesSerial

    def get_object(self):
        queryset = self.get_queryset()
        cpf = self.kwargs['cpf']
        obj = get_object_or_404(queryset, cpf=cpf)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get_queryset(self):
        return Paciente.objects.all()

class ExameAPIView(generics.ListCreateAPIView):
    queryset = Exame.objects.all()
    serializer_class = ExamesSerial
    def create(self, request, *args, **kwargs):
        dados = request.data
        avaliacao = {
            "Pregnancies":int(dados['Pregnancies']),
            "PlasmaGlucose":float(dados['PlasmaGlucose']),
            "DiastolicBloodPressure":float(dados['DiastolicBloodPressure']),
            "TricepsThickness":float(dados['TricepsThickness']),
            "SerumInsulin": float(dados['SerumInsulin']),
            "BMI": float(dados['BMI']),
            "DiabetesPedigree":float(dados['DiabetesPedigree']),
            "Age": int(dados['Age']),
            "Colesterol":float(dados['Colesterol']),
            "HbA1c": float(dados['HbA1c']),
        }
        #Aqui Entra o modelo de machine learning para avaliar se o paciente possui ou não diabetes
        
        print(f"{avaliacao}")

        return super().create(request, *args, **kwargs)

