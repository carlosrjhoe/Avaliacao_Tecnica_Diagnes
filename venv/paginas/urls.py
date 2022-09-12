from django.urls import path
from .views import IndexView, AgendamentoView, PacienteCreate
from .views import PacienteList
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', auth_views.LoginView.as_view(
    #     template_name = 'paginas\index.html'
    # ), name='login'),
    path('agendamento/', PacienteList.as_view(), name='agendamento'),
    path('', PacienteCreate.as_view(), name='cadastrar-paciente'),
]