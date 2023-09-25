from rest_framework import serializers,permissions
from .models import (Paciente,Exame,ConsultaFeedBack)




class  ExamesSerial(serializers.ModelSerializer):
    DataCriacao = serializers.SerializerMethodField()
    class Meta:
        model =Exame
        exclude = ('Atualizacao','ativo')
    
    def get_DataCriacao(self, obj):
        return obj.DataCriacao.strftime('%d/%m/%Y')



class  ExameSerial(serializers.ModelSerializer):
    DataCriacao = serializers.SerializerMethodField()
    class Meta:
        model =Exame
        exclude = ('Atualizacao','Paciente','ativo')
    
    def get_DataCriacao(self, obj):
        return obj.DataCriacao.strftime('%d/%m/%Y')



class PacientesSerial(serializers.ModelSerializer):
    nome = serializers.CharField(source='name_paciente')
    DataCriacao = serializers.SerializerMethodField()
    class Meta:
        extra_kwargs={
            #'cpf':{'write_only':True},
        }
        model =Paciente
        
        fields = (
            'nome',
            'cpf',
            'DataCriacao',
        )
    def get_DataCriacao(self, obj):
       return obj.DataCriacao.strftime('%d/%m/%Y')
class PacienteSerial(serializers.ModelSerializer):
    nome = serializers.CharField(source='name_paciente')
    class Meta:
        extra_kwargs={
            #'cpf':{'write_only':True},
        }
        model =Paciente
        
        fields = (
            'nome',
            'cpf',
            'DataCriacao',
            'Atualizacao',
        )

class PacienteListaExamesSerial(serializers.ModelSerializer):
    '''
      Essa classe se destina a retornar um paciente e todos seus exames
    '''
    nome = serializers.CharField(source='name_paciente')
    exames = ExameSerial(many=True, read_only=True)
    class Meta:
        extra_kwargs={
            #'cpf':{'write_only':True},
        }
        model =Paciente
        
        fields = (
            'nome',
            'cpf',
            'exames'
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