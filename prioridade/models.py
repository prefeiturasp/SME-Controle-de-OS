from django.db import models

class Prioridade(models.Model):
    id_prioridade = models.IntegerField(primary_key= True)
    prioridade = models.CharField(max_length= 50)
