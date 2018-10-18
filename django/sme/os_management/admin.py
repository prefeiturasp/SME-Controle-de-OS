from django.contrib import admin
from sme.os_management.models import (Usuario)

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
  #model:Usuario
  readonly_fields = ['id_divisao']
  list_display = ['usuario_nome', 'usuario_login', 'id_usuario']
  search_fields = ['usuario_nome']
admin.site.register(Usuario, UsuarioAdmin)

