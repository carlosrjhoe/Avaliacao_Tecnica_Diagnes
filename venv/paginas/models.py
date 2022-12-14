from django.db import models
from datetime import datetime
from requests import get


# Create your models here.
class Medico(models.Model):
    ECOCARDIOGRAMA = 'ECOCARDIOGRAMA'
    CLINICO_GERAL = 'CLINICO_GERAL'
    OBSTETRA = 'OBSTETRA'
    
    ESPECIALIDADES_CHOICES = (
        (ECOCARDIOGRAMA, 'Ecocardiografista'),
        (CLINICO_GERAL, 'Clínico Geral'),
        (OBSTETRA, 'Obstetra'),
    )
    
    nome = models.CharField(max_length=30)
    telefone = models.IntegerField()
    email = models.EmailField()
    especialidade = models.CharField(max_length=15, choices=ESPECIALIDADES_CHOICES)
    endereco = models.CharField(max_length=50, verbose_name='endereço')
    cep = models.IntegerField()
    numero = models.IntegerField(verbose_name='número')
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.especialidade}'
    
class Paciente(models.Model):
     
    nome_paciente = models.CharField(max_length=30, blank=False)
    telefone = models.IntegerField(null=True, blank=True)
    data_consulta = models.DateField(max_length=10,null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    
    especialidade = models.ForeignKey(Medico, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f'{self.nome_paciente} - {self.telefone} - {self.data_consulta} - {self.hora}'
    
    def valida_data(self):
        imput_data = get('paciente.data_consulta')
        print(f'{imput_data}')