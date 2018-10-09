import uuid
from django.db import models

# Create your models here.
class Coordenadoria(models.Model):
    id_coord = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    coord_nome = models.CharField(max_length= 100)

class Divisao(models.Model):
    id_divisao = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    id_coord = models.ForeignKey(Coordenadoria, on_delete=models.CASCADE)
    divisao_sigla = models.CharField(max_length= 6)
    divisao_nome = models.CharField(max_length= 100)

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    id_divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE)
    usuario_login = models.CharField(max_length=10)
    usuario_nome = models.CharField(max_length=100)