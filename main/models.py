from django.db import models
from accounts.models import * # Organization, Volunteer

class Volunteer_Project(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    urgencia = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # escala de 1 a 5
    organizacao = models.ForeignKey(Organization, on_delete=models.CASCADE)  # relacionamento 1:N c a organização
    voluntarios = models.ManyToManyField(Volunteer)  # relacionamento N:N com os voluntários
    data_criacao = models.DateTimeField(auto_now_add=True)
    
def qtd_volunteers(self):
        # voluntários inscritos ao projeto
        return self.voluntarios.count()

def duration(self):
    return self.data_fim - self.data_inicio
def __str__(self):
    return self.nome
