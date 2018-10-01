from django.db import models
from coordenadorias.models import Coordenadoria

class Divisao(models.Model):
    id_divisao = models.IntegerField(primary_key= True)
    id_coord = models.ForeignKey(Coordenadoria, on_delete=models.CASCADE)
    sigla = models.CharField(max_length= 6)
    nome_divisao = models.CharField(max_length= 100)
    

