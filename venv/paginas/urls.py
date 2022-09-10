from django.urls import path
from .views import IndexView, AgendamentoView, PacienteCreate
from .views import PacienteList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('agendamento/', PacienteList.as_view(), name='agendamento'),
    path('form/', PacienteCreate.as_view(), name='cadastrar-paciente'),
]