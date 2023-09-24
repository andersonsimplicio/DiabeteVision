from django.contrib import admin
from .models import Paciente, Exame, ConsultaFeedBack

# Define a custom admin class for Paciente
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name_paciente', 'cpf', 'ativo', 'DataCriacao')
    list_filter = ('ativo', 'DataCriacao')
    search_fields = ('name_paciente', 'cpf')
    list_per_page = 20

# Define a custom admin class for Exame
class ExameAdmin(admin.ModelAdmin):
    list_display = ('get_paciente_name', 'Diabetic')
    list_filter = ('Diabetic',)
    search_fields = ('Paciente__name_paciente', 'Diabetic')
    list_per_page = 20
    def get_paciente_name(self, obj):
        return obj.Paciente.name_paciente
    get_paciente_name.short_description = 'Nome do Paciente'
    get_paciente_name.admin_order_field = 'Paciente__name_paciente'
    
# Define a custom admin class for ConsultaFeedBack
class ConsultaFeedBackAdmin(admin.ModelAdmin):
    list_display = ('IdPaciente', 'DataCriacao', 'Exame', 'FeedBackDiabetci')
    list_filter = ('DataCriacao', 'FeedBackDiabetci')
    search_fields = ('IdPaciente__name_paciente', 'Exame__Paciente__name_paciente', 'FeedBackDiabetci')
    list_per_page = 20

# Register the custom admin classes with the models
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Exame, ExameAdmin)
admin.site.register(ConsultaFeedBack, ConsultaFeedBackAdmin)

