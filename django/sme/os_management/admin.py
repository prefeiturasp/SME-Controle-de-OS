from django.contrib import admin
from sme.os_management.models import (Usuario)

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
  #model:Usuario
  list_display = ['usuario_nome', 'usuario_login']
  search_fields = ['usuario_nome']
admin.site.register(Usuario, UsuarioAdmin)

