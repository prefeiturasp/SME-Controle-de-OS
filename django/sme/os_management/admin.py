from django.contrib import admin
from sme.os_management.models import Usuario, Divisao, Coordenadoria

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