from django.db import models

class Administrativo(models.Model):
    id_processo_adm = models.IntegerField(primary_key= True)
    processo_adm = models.CharField(max_length= 20)
