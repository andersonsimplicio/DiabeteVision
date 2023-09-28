from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User 
from rest_framework import status
from .models import Exame,Paciente
from django.urls import reverse
from .RandomForest import Brain

class ExameAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='anderson', password='###')
        self.paciente = Paciente.objects.create(
            name_paciente="PacienteTest",
            cpf="12345678901"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = reverse('exames')
        self.brain = Brain()#Carga do modelo de Machine Learning

    def test_criar_exame_com_previsao_diabetes(self):

        dados = {
            "Paciente": self.paciente.Id,
            "Pregnancies": 3,
            "PlasmaGlucose": 102.0,
            "DiastolicBloodPressure": 100.0,
            "TricepsThickness": 25.0,
            "SerumInsulin": 289.0,
            "BMI": 42.19,
            "DiabetesPedigree": 0.18,
            "Age": 43,
            "Colesterol": 218.46,
            "HbA1c": 9.04,
        }

        response = self.client.post(self.url, data=dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        exame_criado = Exame.objects.get(Paciente=self.paciente.Id)
        self.assertEqual(exame_criado.Diabetic, 1)
       
    def test_criar_exame_sem_previsao_diabetes(self):
        dados = {
            "Paciente": self.paciente.Id,
            "Pregnancies": 0,
            "PlasmaGlucose": 98.0,
            "DiastolicBloodPressure": 80.0,
            "TricepsThickness": 34.0,
            "SerumInsulin": 23.0,
            "BMI": 43.50,
            "DiabetesPedigree": 1.20,
            "Age": 21,
            "Colesterol": 192.0,
            "HbA1c": 3.30,
        }

        response = self.client.post(self.url, data=dados, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exame_criado = Exame.objects.get(Paciente=self.paciente.Id)
        print(f"{exame_criado.Pregnancies}")
       
        exame_criado = Exame.objects.first()
        self.assertEqual(exame_criado.Diabetic, 0) # type: ignore
    
    def test_modelo_random_fofrest(self):
        dados = [
            {
            #Com diabetes
            "Pregnancies": 0,
            "PlasmaGlucose": 98.0,
            "DiastolicBloodPressure": 80.0,
            "TricepsThickness": 34.0,
            "SerumInsulin": 23.0,
            "BMI": 43.50,
            "DiabetesPedigree": 1.20,
            "Age": 21,
            "Colesterol": 192.0,
            "HbA1c": 3.3
            },
            {
            #Sem diabetes
            "Pregnancies": 3,
            "PlasmaGlucose": 102.0,
            "DiastolicBloodPressure": 100.0,
            "TricepsThickness": 25.0,
            "SerumInsulin": 289.0,
            "BMI": 42.19,
            "DiabetesPedigree": 0.18,
            "Age": 43,
            "Colesterol": 218.46,
            "HbA1c": 9.04,
            },
             {
            #Com diabetes
            "Pregnancies": 3,
            "PlasmaGlucose": 102.0,
            "DiastolicBloodPressure": 100.0,
            "TricepsThickness": 25.0,
            "SerumInsulin": 289.0,
            "BMI": 42.19,
            "DiabetesPedigree": 0.18,
            "Age": 43,
            "Colesterol": 218.46,
            "HbA1c": 9.04,
            },
             {
            #Sem diabetes
            "Pregnancies": 1,
            "PlasmaGlucose": 85.0,
            "DiastolicBloodPressure": 70.0,
            "TricepsThickness": 30.0,
            "SerumInsulin": 70.0,
            "BMI": 25.0,
            "DiabetesPedigree": 0.2,
            "Age": 28,
            "Colesterol": 180.0,
            "HbA1c": 5.0,
            }
        ]
        previsao =[]
        for _ in dados:
           previsao.append(self.brain.predict(_)[0]) # type: ignore
        self.assertEqual([0,1,1,0], previsao) # type: ignore

    def tearDown(self):
        # Deleta o objeto Paciente ao final do teste
        self.paciente.delete()