from django.db import models

class Fase(models.Model):
    id_fase = models.IntegerField(primary_key= True)
    fase = models.CharField(max_length= 100)
    
