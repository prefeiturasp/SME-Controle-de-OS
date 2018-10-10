from django.db import models
import uuid

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

class Fornecedor(models.Model):
    id_fornecedor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome_atendente = models.CharField(max_length= 100)
    empresa = models.CharField(max_length= 100)
    funcao = models.CharField(max_length= 100)


class TermoContrato(models.Model):

    id_termo_contrato = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    termo_contrato = models.CharField(max_length= 20)

class TermoAditivo(models.Model):
    id_termo_contrato_ad =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    termo_contrato_aditivo = models.CharField(max_length= 20)

class Prioridade(models.Model):
    id_prioridade = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    prioridade = models.CharField(max_length= 50)


class TipoServico(models.Model):
    id_tipo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tipo = models.CharField(max_length= 100)


class Sistema(models.Model):
    id_sistema = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sistema = models.CharField(max_length= 100)

class Fase(models.Model):
    id_fase = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    fase = models.CharField(max_length= 100)


class Status(models.Model):
    id_status = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length= 100)


class Login(models.Model):
    login =  models.CharField(max_length= 12)
    senha = models.IntegerField()


class Administrativo(models.Model):
    id_processo_adm = models.IntegerField(primary_key= True)
    processo_adm = models.CharField(max_length= 20)

class Demandante(models.Model):
    id_area_demandante = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    id_divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE)

class CadastroOS(models.Model):
    n_os = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    id_processo_adm = models.ForeignKey(Administrativo, on_delete= models.CASCADE)
    id_termo_contrato = models.ForeignKey(TermoContrato, on_delete= models.CASCADE)
    termo_aditivo_contrato = models.ForeignKey(TermoAditivo, on_delete= models.CASCADE)
    id_demandante = models.ForeignKey(Demandante, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length= 100)
    id_prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    dt_necessidade = models.DateField()
    solicitacao = models.TextField(max_length= 100)
    esforco_estimado = models.IntegerField()
    esforco_realizado= models.IntegerField()
    esforco_relacionamento = models.IntegerField()
    dt_entrega = models.DateField()
    dt_aceite = models.DateField()
    ss_prestador_servico = models.CharField(max_length= 10)
    mes_fatura = models.CharField(max_length= 10)
    ano_fatura = models.IntegerField()
    observacao = models.TextField(max_length= 100)

class Movimentacao(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    n_os = models.ForeignKey(CadastroOS, on_delete= models.CASCADE)
    movimentacao = models.CharField(max_length= 100)
    dt_movimentacao = models.DateField()


