from django.http import Http404, QueryDict
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.db.models import F
from rest_framework.response  import Response
from .RandomForest import Brain
from .models import (
    Paciente,
    Exame,
   )

from .serialize import (
    PacientesSerial,
    PacienteListaExamesSerial,
    ExamesSerial,  
    ExameUpdateSerial,
    ExameListSerial
)

class PacientesAPIView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacientesSerial


class PacienteAPIView(generics.RetrieveAPIView):
    serializer_class = PacienteListaExamesSerial
    lookup_field = 'cpf'
    
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
        #Aqui Entra o modelo de machine learning para avaliar se o 
        # paciente possui ou não diabetes
        rf = Brain()
        previsao = rf.predict(avaliacao)
        if previsao is not None:
            if isinstance(request.data, QueryDict):
                request.data._mutable = True
                request.data['Diabetic'] = int(previsao[0])  # type: ignore
                return super().create(request, *args, **kwargs)
        else:
            return super().create(request, *args, **kwargs)


class ExameFeedbackAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exame.objects.all()
    serializer_class =ExameUpdateSerial

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        feedback = request.data.get('Feedback')
        if feedback is not None:
            instance.Feedback = feedback
            instance.HouveFeedback = True
            instance.save()
        self.perform_update(serializer)
        return Response(serializer.data)

class ExamesListaFeedbackAPIView(generics.ListAPIView):
    
    serializer_class =ExameListSerial

    def get_queryset(self):
       return Exame.objects.filter(HouveFeedback=True).exclude(Diabetic=F('Feedback'))

    