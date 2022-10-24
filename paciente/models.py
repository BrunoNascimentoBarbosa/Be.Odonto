from decimal import DefaultContext
from tabnanny import verbose
from django.conf import settings
from django.db import models
from CadastroDentistas.models import Dentista
from django.contrib.auth.models import User

 
class paciente(models.Model):
    SEXO_CHOICES = (
        ("F","Feminino"),
        ("M","Masculino"),
    )
    OPTION = (
        ("S","Sim"),
        ("N","Não")
    )
    STATUS = (
        ("A","Em andamento"),
        ("P","Parado"),
        ("c","Concluído"),
    )
    nome = models.CharField(max_length=100,blank=False, null=False)
    sobrenome = models.CharField(max_length=100,blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    diabetico = models.CharField(max_length=1,choices=OPTION,blank=False, null=False)
    hipertenso = models.CharField(max_length=1,choices=OPTION,blank=False, null=False)
    alergia_a_medicamentos = models.CharField(max_length=100, default='não') 
    outras_observacoes = models.CharField(max_length=200,blank=True, default='não', verbose_name='Observações') 
    dentista = models.ForeignKey(Dentista, on_delete=models.PROTECT)
    tratamento = models.CharField(max_length=1,choices=STATUS, blank=True,null=False)
    historico = models.TextField(max_length=3000)

    class Meta:
        # Ordena por nome
        ordering = ('nome',)
    
    
    #Essa configuração tá sendo sobreposta pelo list_display no arquivo admin.
    #video mostra como trabalhar isso no model.
    #https://www.youtube.com/watch?v=1KpQfuWloWA
    def __str__(self):
        return self.nome + ' ' + self.sobrenome  

class consulta(models.Model):
    paciente = models.ForeignKey(paciente,related_name="consulta" ,on_delete=models.PROTECT)
    historico_consulta = models.TextField(max_length=3000)
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.paciente)

 