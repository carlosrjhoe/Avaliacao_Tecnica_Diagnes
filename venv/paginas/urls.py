from django.urls import path
from .views import IndexView, AgendamentoView, PacienteCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('agendamento/', AgendamentoView.as_view(), name='agendamento'),
    path('form/', PacienteCreate.as_view(), name='cadastrar-paciente'),
]