from django.urls import path
from .views import IndexView, AgendamentoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('agendamento/', AgendamentoView.as_view(), name='agendamento'),
]