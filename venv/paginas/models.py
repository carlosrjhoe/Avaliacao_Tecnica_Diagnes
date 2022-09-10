from django.db import models

# Create your models here.
class Medico(models.Model):
    
    ESPECIALIDADES_CHOICES = (
        ('E', 'Ecocardiografista'),
        ('C', 'Clínico Geral'),
        ('O', 'Obstetra'),
    )
    
    nome = models.CharField(max_length=30)
    telefone = models.IntegerField()
    email = models.EmailField()
    especialidade = models.CharField(max_length=1, choices=ESPECIALIDADES_CHOICES, blank=False, null=False)
    endereco = models.CharField(max_length=50, verbose_name='endereço')
    cep = models.IntegerField()
    numero = models.IntegerField(verbose_name='número')
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.telefone} - {self.email} - {self.especialidade} - {self.endereco} - {self.cep} - {self.numero} - {self.bairro} - {self.cidade} - {self.estado}'
    
class Paciente(models.Model):
    
    ESPECIALIDADES_CHOICES = (
        ('E', 'Ecocardiografista'),
        ('C', 'Clínico Geral'),
        ('O', 'Obstetra'),
    )
     
    nome_paciente = models.CharField(max_length=30)
    telefone = models.IntegerField(max_length=11)
    data_consulta = models.DateField(null=False)
    hora = models.TimeField()
    
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f'{self.nome_paciente} - {self.telefone} - {self.data_consulta} - {self.hora}'