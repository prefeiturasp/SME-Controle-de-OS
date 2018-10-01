from django.db import models
from usuario.models import Usuario
from cadastro.models import Cadastro

class Movimentacao(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    n_os = models.ForeignKey(Cadastro, on_delete= models.CASCADE)
    movimentacao = models.CharField(max_length= 100)
    dt_movimentacao = models.DateField()

