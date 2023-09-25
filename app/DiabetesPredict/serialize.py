from rest_framework import serializers,permissions
from .models import (Paciente,Exame)




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

class  ExameUpdateSerial(serializers.ModelSerializer):
    DataCriacao = serializers.SerializerMethodField()
    Paciente_nome = serializers.SerializerMethodField() 
    class Meta:
        model =Exame
        fields = [
                  'Id', 
                  'DataCriacao', 
                  'Paciente',
                  'Paciente_nome', 
                  'Pregnancies',
                  'PlasmaGlucose',
                  'DiastolicBloodPressure',
                  'TricepsThickness',
                  'SerumInsulin',
                  'BMI',
                  'DiabetesPedigree',
                  'Age',
                  'Colesterol',
                  'HbA1c',
                  'Diabetic',
                  'Feedback', 
                  'HouveFeedback']
    
    def get_DataCriacao(self, obj):
        return obj.DataCriacao.strftime('%d/%m/%Y')

    def update(self, instance, validated_data):
        feedback = validated_data.get('Feedback')
        if feedback is not None:
            instance.Feedback = feedback
            instance.HouveFeedback = True  # Define HouveFeedback como True
            instance.save()
        return instance
    
    def get_Paciente_nome(self, obj):
        paciente_id = obj.Paciente.Id
        paciente = Paciente.objects.get(Id=paciente_id)
        return paciente.name_paciente  


class  ExameListSerial(serializers.ModelSerializer):
    Atualizacao = serializers.SerializerMethodField()
    Paciente_nome = serializers.SerializerMethodField() 
    class Meta:
        model =Exame
        fields = [
                  'Id', 
                  'Atualizacao', 
                  'Paciente_nome', 
                  'Feedback', 
                  'Diabetic',
                  ]
    
    def get_Atualizacao(self, obj):
        return obj.Atualizacao.strftime('%d/%m/%Y')
        
    def get_Paciente_nome(self, obj):
        paciente_id = obj.Paciente.Id
        paciente = Paciente.objects.get(Id=paciente_id)
        return paciente.name_paciente 




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



