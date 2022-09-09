from django.urls import path
from .views import CampoCreate, EnderecoCreate
from .views import CampoUpdate, EnderecoUpdate


urlpatterns = [
    path('cadastro/campo', CampoCreate.as_view(), name='cadastro-campo'),
    path('cadastro/endereco', EnderecoCreate.as_view(), name='cadastro-endereco'),
    
    path('editar/campo/<int:pk>', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/endereco/<int:pk>', EnderecoUpdate.as_view(), name='editar-endereco'),
]