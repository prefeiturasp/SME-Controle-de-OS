from django.contrib import admin
from sme.os_management.models import (Usuario, Divisao, Coordenadoria, Fornecedor, TermoContrato, TermoAditivo,
Prioridade, TipoServico, Sistema, Fase, Status, Login, Administrativo, Demandante, CadastroOS, Movimentacao)

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
  #model:Usuario
  readonly_fields = ['id_divisao']
  list_display = ['usuario_nome']
  search_fields = ['usuario_nome']
admin.site.register(Usuario, UsuarioAdmin)

class DivisaoAdmin(admin.ModelAdmin):
  #model:Divisao
  readonly_fields = ['id_divisao']
  list_display = ['divisao_nome', 'divisao_sigla', 'coordenadoria_nome']
  search_fields = ['divisao_nome', 'divisao_sigla']

  def coordenadoria_nome(self, instance):
        return instance.id_coord.coord_nome

admin.site.register(Divisao, DivisaoAdmin)

class CoordenadoriaAdmin(admin.ModelAdmin):
  #model:Coordenadoria
  readonly_fields = ['id_coord']
  list_display = ['coord_nome']
  search_fields = ['coord_nome']
admin.site.register(Coordenadoria, CoordenadoriaAdmin)

class FornecedorAdmin(admin.ModelAdmin):
  readonly_fields = ['id_fornecedor']
  list_display = ['empresa']
  search_fields = ['empresa']
admin.site.register(Fornecedor, FornecedorAdmin)


class TermoContratoAdmin(admin.ModelAdmin):
  readonly_fields = ['id_termo_contrato']
  list_display = ['termo_contrato']
  search_fields = ['id_termo_contrato']
admin.site.register(TermoContrato, TermoContratoAdmin)

#class TermoAditivoAdmin(admin.ModelAdmin):
 # readonly_fields = ['id_termo_contrato_ad']
  #list_display = ['termo_contrato_ad']
  #search_fields = ['id_termo_contrato_ad']
#admin.site.register(TermoAditivo, TermoContratoAdmin)

class PrioridadeAdmin(admin.ModelAdmin):
  readonly_fields = ['id_prioridade']
  list_display = ['prioridade']
  search_fields = ['id_prioridade']
admin.site.register(Prioridade, PrioridadeAdmin)


class TipoServicoAdmin(admin.ModelAdmin):
  readonly_fields = ['id_tipo']
  list_display = ['tipo']
  search_fields = ['id_tipo']
admin.site.register(TipoServico, TipoServicoAdmin)

class SistemaAdmin(admin.ModelAdmin):
  readonly_fields = ['id_sistema']
  list_display = ['sistema']
  search_fields = ['id_sistema']
admin.site.register(Sistema, SistemaAdmin)


class FaseAdmin(admin.ModelAdmin):
  readonly_fields = ['id_fase']
  list_display = ['fase']
  search_fields = ['id_fase']
admin.site.register(Fase, FaseAdmin)


class StatusAdmin(admin.ModelAdmin):
  readonly_fields = ['id_status']
  list_display = ['status']
  search_fields = ['id_status']
admin.site.register(Status, StatusAdmin)


#class LoginAdmin(admin.ModelAdmin):
 # readonly_fields = ['login']
  #list_display = ['login, senha']
  #search_fields = ['login']
#admin.site.register(Login, LoginAdmin)


class AdministrativoAdmin(admin.ModelAdmin):
  readonly_fields = ['id_processo_adm']
  list_display = ['processo_adm']
  search_fields = ['id_processo_adm']
admin.site.register(Administrativo, AdministrativoAdmin)


#class CadastroOSAdmin(admin.ModelAdmin):
 # readonly_fields = ['n_os']
  #list_display = ['id_processo_adm , id_termo_contrato, termo_aditivo_contrato, id_demandante, responsavel, id_prioridade, id_tipo, id_sistema, dt_necessidade, solicitacao ']
  #search_fields = ['n_os']
#admin.site.register(CadastroOS, CadastroOSAdmin)


#class MovimentacaoAdmin(admin.ModelAdmin):
 # list_display = ['n_os, movimentacao, dt_movimentacao']
  #search_fields = ['n_os']
#admin.site.register(Movimentacao, MovimentacaoAdmin)

