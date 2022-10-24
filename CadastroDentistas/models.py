from django.db import models


class Especialidades(models.Model):
    especialidade = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Especialidade'

    def __str__(self):
        return self.especialidade

class Dentista(models.Model):
    SEXO_CHOICES = (
        ("F","Feminino"),
        ("M","Masculino"),
    )
    nome = models.CharField(max_length=100,blank=False, null=False)
    sobrenome = models.CharField(max_length=100,blank=False, null=False)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    CRO = models.CharField(max_length=7,blank=False, null=False)
    especialidade =models.ForeignKey(Especialidades,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Drª" + " "+ self.nome +" "+ self.sobrenome



