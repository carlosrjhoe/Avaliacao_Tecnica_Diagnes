from django.views.generic.edit import CreateView, UpdateView
from .models import Cadastro_medicos
from django.urls import reverse_lazy

# Create your views here.
class MedicosCreate(CreateView):
    model = Cadastro_medicos
    fields = ['nome', 'telefone','email','especialidade','cep','logradouro','numero','bairro','cidade','estado',]
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')
    
    
################### UPDATE #######################

class MedicosUpdate(UpdateView):
    model = Cadastro_medicos
    fields = ['nome', 'telefone','email','especialidade',]
    template_name = 'paginas/index.html'
    success_url = reverse_lazy('index')
    