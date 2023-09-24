from rest_framework.views import APIView
from rest_framework.response  import Response
from .models import (
    Paciente,
    Exame,
    ConsultaFeedBack
)

from .serialize import (
    PacienteSerial,
    ExameSerial,
    ConsultaFeedBackSerial
)

class PacienteApiView(APIView):
    '''
     Api View de Pacientes lista todos pacientes
    '''
    def get(self,request):
        pacientes = Paciente.objects.all()
        serializer = PacienteSerial(pacientes,many=True)
        return Response(serializer.data)

class ExameApiView(APIView):
    '''
     Api View de Pacientes lista todos pacientes
    '''
    def get(self,request):
        exame = Exame.objects.all()
        serializer = ExameSerial(exame,many=True)
        return Response(serializer.data)


