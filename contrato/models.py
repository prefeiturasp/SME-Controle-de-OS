from django.db import models

# Create your models here.
class TermoContrato(models.Model):
    id_termo_contrato = models.IntegerField(primary_key= True)
    termo_contrato = models.CharField(max_length= 20)


class TermoAditivo(models.Model):
    id_termo_contrato_ad =  models.IntegerField(primary_key= True)
    termo_aditivo_contrato = models.CharField(max_length= 20)
    