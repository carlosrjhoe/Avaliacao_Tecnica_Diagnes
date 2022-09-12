from msilib.schema import Class
from pipes import Template
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Paciente

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/login.html'
    
class AgendamentoView(TemplateView):
    template_name = 'paginas/agendamento.html'


#################### CREATE ####################

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nome_paciente','telefone','data_consulta','hora','especialidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('agendamento')
    

#################### LIST ####################

class PacienteList(ListView):
    model = Paciente
    template_name = 'paginas/agendamento.html'
    
