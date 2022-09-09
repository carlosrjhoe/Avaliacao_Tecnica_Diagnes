from operator import index
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

# class AgendamentoView(TemplateView):
#     template_name = 'paginas/agendamento.html'

# class ListagemView(TemplateView):
#     template_name = 'paginas/listagem.html'