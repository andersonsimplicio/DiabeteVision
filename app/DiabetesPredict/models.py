from django.db import models
import uuid


class Base(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DataCriacao = models.DateTimeField(auto_now_add=True)
    Atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Paciente(Base):
    '''
     Essa classe se destina a armazenar as informações do usuário como 
     nome e cpf
    '''
    name_paciente = models.CharField(verbose_name='Nome do Paciente',max_length=255)
    cpf = models.CharField(verbose_name='CPF',max_length=11)
    
    def __str__(self):
        return f"Paciente {self.Id} - {self.name_paciente}"

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Exame(Base):
    '''
    Essa classe se destina a armazenar os exames que o paciente possa ter, 
    são esses dados que irão ser avaliados pela IA, o resultado será armazenado no campo
    Diabetic
    '''
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='exames')
    Pregnancies = models.IntegerField(
        verbose_name='Número de Gestações',
        default=0,
        blank=True,
        null=True,
    )
    PlasmaGlucose = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Plasma Glucose')
    DiastolicBloodPressure = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Pressão Arterial Diastólica')
    TricepsThickness = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra da Pele do Tríceps')
    SerumInsulin = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Insulina Sérica')
    BMI = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Índice de Massa Corporal')
    DiabetesPedigree = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Historico Familiar')
    Age = models.IntegerField(verbose_name='Idade')
    Colesterol = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Colesterol LDL')
    HbA1c = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='HbA1c')
    Diabetic = models.IntegerField(verbose_name='Diabético',default=0,blank=True,null=True)

    Feedback = models.IntegerField(verbose_name='Feedback', default=0, choices=[(0, '0'), (1, '1')])
    HouveFeedback = models.BooleanField(verbose_name='Houve Feedback', default=False)
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
    
   
    def __str__(self):
        return f" Exame ID:{self.Id} - Paciente {self.Paciente.name_paciente} - Diabético: {self.Diabetic}" 

 




