from django.views.generic.edit import CreateView, UpdateView
from .models import Campo, Endereco
from django.urls import reverse_lazy

# Create your views here.
class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'telefone','email','especialidade',]
    template_name = 'paginas/index.html'
    success_url = reverse_lazy('index')
    
class EnderecoCreate(CreateView):
    model = Campo
    fields = ['cep','logradouro','numero','bairro','cidade','estado',]
    template_name = 'paginas/index.html'
    success_url = reverse_lazy('index')
    
################### UPDATE #######################

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'telefone','email','especialidade',]
    template_name = 'paginas/index.html'
    success_url = reverse_lazy('index')
    
class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['cep','logradouro','numero','bairro','cidade','estado',]
    template_name = 'paginas/index.html'
    success_url = reverse_lazy('index')