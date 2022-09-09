from tabnanny import verbose
from django.db import models

# Create your models here.
class Cadastro_medicos(models.Model):
    
    ESPECIALIDADE = (
        ('E', 'Ecocardiografista'),
        ('C', 'Clínico Geral'),
        ('O', 'Obstetra'),
    )
    
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=1, choices=ESPECIALIDADE)
    cep = models.IntegerField()
    logradouro = models.IntegerField()
    numero = models.IntegerField(verbose_name="Número")
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.telefone} - {self.email} - {self.especialidade} - {self.cep} - {self.logradouro} - {self.numero} - {self.bairro} - {self.cidade} - {self.estado}'
    