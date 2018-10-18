from django import forms
from .models import Login, CadastroOS


class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('login', 'senha',)

class CadastroOSForm(forms.ModelForm):

    class Meta:
        model = CadastroOS
        fields = ('responsavel', 'dt_necessidade', 'solicitacao', 'esforco_estimado', 'esforco_realizado',
         'esforco_relacionamento', 'dt_entrega', 'ss_prestador_servico', 'mes_fatura', 'ano_fatura', 'observacao',)