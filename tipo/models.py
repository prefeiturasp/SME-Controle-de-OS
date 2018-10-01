from django.db import models

class Tipo_Serv(models.Model):
    id_tipo = models.IntegerField(primary_key= True)
    tipo = models.CharField(max_length= 100)
    
