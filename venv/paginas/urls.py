from django.urls import path
from .views import IndexView, AgendamentoView, ListagemView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('agendamento/', AgendamentoView.as_view(), name='agendamento'),
    path('listagem/', ListagemView.as_view(), name='listagem'),
]