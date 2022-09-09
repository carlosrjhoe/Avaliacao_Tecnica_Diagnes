from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Campo(models.Model):
    
    ESPECIALIDADE = (
        ('E', 'Ecocardiografista'),
        ('C', 'Clínico Geral'),
        ('O', 'Obstetra'),
    )
    
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=1, choices=ESPECIALIDADE)
    
    def __str__(self) -> str:
        return f'{self.nome}{self.telefone}{self.email}{self.especialidade}'
    
class Endereco(models.Model):
    
    cep = models.IntegerField()
    logradouro = models.IntegerField()
    numero = models.IntegerField(verbose_name="Número")
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2)
    
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f'{self.nome}, ({self.campo})'