from django.db import models

from divisoes.models import Divisao

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key= True)
    login = models.CharField(max_length=10)
    nome_usuario = models.CharField(max_length=100)
    id_divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE)


