from django.db import models

id_fornecedor = models.IntegerField(primary_key= True, max_length= 5)
nome_atendente = models.CharField(max_length= 100)
empresa = models.CharField(max_length= 100)
funcao = models.CharField(max_length= 100)
