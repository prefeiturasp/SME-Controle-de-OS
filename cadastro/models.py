from django.db import models
from demandante.models import Demandante
from prioridade.models import Prioridade
from tipo.models import Tipo_Serv
from sistema.models import Sistema
from fase.models import Fase
from administrativo.models import Administrativo 
from contrato.models import TermoAditivo
from contrato.models import TermoContrato

class Cadastro(models.Model):

    n_os = models.IntegerField(primary_key= True)
    id_processo_adm = models.ForeignKey(Administrativo, on_delete= models.CASCADE)
    id_termo_contrato = models.ForeignKey(TermoContrato, on_delete= models.CASCADE)
    termo_aditivo_contrato = models.ForeignKey(TermoAditivo, on_delete= models.CASCADE)
    dt_emissao = models.DateField()
    id_ad = models.ForeignKey(Demandante, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length= 100)
    id_priori = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo_Serv, on_delete=models.CASCADE)
    id_sist = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    dt_nece = models.DateField()
    solicitacao = models.TextField(max_length= 100)
    estima_esforco = models.IntegerField()
    reali_esforco = models.IntegerField()
    esforco_relacio = models.IntegerField()
    dt_entrega = models.DateField()
    dt_aceite = models.DateField()
    id_fase = models.ForeignKey(Fase, on_delete= models.CASCADE)
    ss_presta_serv = models.CharField(max_length= 10)
    mes_fatura = models.CharField(max_length= 10)
    ano_fatura = models.IntegerField()
    obs = models.TextField(max_length= 100)