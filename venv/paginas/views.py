from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Medico, Paciente

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'
    
class AgendamentoView(TemplateView):
    template_name = 'paginas/agendamento.html'


#################### CREATE ####################

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nome_paciente','telefone','data_consulta','hora','medico']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')