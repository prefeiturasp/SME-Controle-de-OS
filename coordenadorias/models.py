from django.db import models

class Coordenadoria(models.Model):
    id_coord = models.IntegerField(primary_key= True)
    nome_coord = models.CharField(max_length= 100)
