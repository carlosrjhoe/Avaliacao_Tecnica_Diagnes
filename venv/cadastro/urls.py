from django.urls import path
from .views import MedicosCreate, MedicosUpdate


urlpatterns = [
    path('cadastro/Cadastro_medicos/', MedicosCreate.as_view(), name='cadastro-campo'),
    path('editar/Cadastro_medicos/<int:pk>', MedicosUpdate.as_view(), name='editar-campo'),
]