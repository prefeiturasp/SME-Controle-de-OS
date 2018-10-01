from django.db import models
from divisoes.models import Divisao

class Demandante(models.Model):
    id_area_demandante = models.IntegerField(primary_key= True)
    id_divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE)
