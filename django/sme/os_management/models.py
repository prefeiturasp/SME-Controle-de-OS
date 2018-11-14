from django.db import models
#from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)

TIPO_CHOICES = (
    ('CORRECAO', 'Correção'),
    ('EVOLUCAO', 'Evolução'),

)

class Coordenadoria(models.Model):
    coord_nome = models.CharField(max_length= 100)

class Divisao(models.Model):
    divisao_sigla = models.CharField(max_length= 6)
    divisao_nome = models.CharField(max_length= 100)

class Usuario(models.Model): #AbstractBaseUser, PermissionsMixin
    usuario_login = models.CharField(max_length=10)
    usuario_nome = models.CharField(max_length=100, unique=True)
   # ativo = models.BooleanField('Está ativo?', blank=True, default=True)
    #equipe = models.BooleanField('É admin?')
    #data_cadastro = models.DateTimeField('Data de entrada', auto_now_add=True)

    #object = UserManager

class Fornecedor(models.Model):
    nome_atendente = models.CharField(max_length= 100)
    empresa = models.CharField(max_length= 100)
    funcao = models.CharField(max_length= 100)

class TermoContrato(models.Model):
    termo_contrato = models.CharField(max_length= 20)

class TermoAditivo(models.Model):
    termo_contrato_aditivo = models.CharField(max_length= 20)


class TipoServico(models.Model):
    tipo = models.CharField(max_length= 100, choices= TIPO_CHOICES)


class Sistema(models.Model):
    sistema = models.CharField(max_length= 100)

class Fase(models.Model):
    fase = models.CharField(max_length= 100)


class Status(models.Model):
    status = models.CharField(max_length= 100)


class MeuLogin(models.Model):
    login =  models.CharField(max_length= 12)
    senha = models.CharField(max_length= 10)

class Administrativo(models.Model):
    processo_adm = models.CharField(max_length= 20, verbose_name='Processo Administrativo')

class Demandante(models.Model):
    demandante = models.CharField(max_length=20,)

class CadastroOS(models.Model):
    n_os = models.IntegerField() 
    processo_adm = models.ForeignKey(Administrativo, on_delete= models.CASCADE)
    termo_contrato = models.ForeignKey(TermoContrato, on_delete= models.CASCADE, verbose_name='Termo de Contrato')
    termo_contrato_aditivo = models.ForeignKey(TermoAditivo, on_delete= models.CASCADE, verbose_name= 'Termo Aditivo de Contrato')
    demandante = models.ForeignKey(Demandante, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length= 100,verbose_name='Responsável')
    prioridade = models.BooleanField('Emergencial', default=False)
    tipo = models.ForeignKey(TipoServico, on_delete=models.CASCADE, verbose_name='Tipo de Serviço')
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    data_necessidade = models.DateField(verbose_name='Data da necessidade')
    solicitacao = models.TextField(max_length= 1500,verbose_name='Solicitação')
    esforco_estimado = models.IntegerField(verbose_name='Esforço estimado')
    esforco_realizado= models.IntegerField(verbose_name='Esforço realizado')
    esforco_relacionamento = models.IntegerField(verbose_name='Esforço Relacionamento')
    data_entrega = models.DateField(verbose_name='Data de entrega')
    data_aceite = models.DateField(verbose_name='Data de aceite')
    ss_prestador_servico = models.CharField(max_length= 10)
    fase = models.ForeignKey(Fase, on_delete= models.CASCADE)
    status = models.ForeignKey(Status, on_delete= models.CASCADE)
    mes_fatura = models.CharField(max_length= 10, verbose_name='Mês fatura')
    ano_fatura = models.IntegerField()
    observacao = models.TextField(max_length= 500, verbose_name='Observação')

class Movimentacao(models.Model):
    n_os = models.ForeignKey(CadastroOS, on_delete= models.CASCADE)
    movimentacao = models.CharField(max_length= 100)
    data_movimentacao = models.DateField()


