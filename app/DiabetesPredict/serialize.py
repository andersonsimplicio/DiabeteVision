from rest_framework import serializers,permissions
from .models import (Paciente,Exame,ConsultaFeedBack)


class PacienteSerial(serializers.ModelSerializer):
    nome = serializers.CharField(source='name_paciente')
    class Meta:
        extra_kwargs={
            'cpf':{'write_only':True},
        }
        model =Paciente
        
        fields = (
            'nome',
            'cpf',
            'DataCriacao',
            'Atualizacao',
        )

class  ExameSerial(serializers.ModelSerializer):
    class Meta:
        model =Exame
        fields = (
                'Id',
                'Paciente',
                'Pregnancies',
                'PlasmaGlucose',
                'DiastolicBloodPressure',
                'TricepsThickness',
                'SerumInsulin' ,
                'BMI',
                'DiabetesPedigree' ,
                'Age',
                'Colesterol',
                'HbA1c',
                'Diabetic'
            )

class ConsultaFeedBackSerial(serializers.ModelSerializer):
    class Meta:
        model = ConsultaFeedBack
        fields =(
            'IdPaciente',
            'DataConsulta',  
            'Exame',
            'FeedBackDiabetci'
        )