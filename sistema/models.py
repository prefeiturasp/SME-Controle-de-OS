from django.db import models

class Sistema(models.Model):
    id_sistema = models.IntegerField(primary_key= True)
    sistema = models.CharField(max_length= 100)