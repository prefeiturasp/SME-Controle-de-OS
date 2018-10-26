from django import forms
from .models import (Login, CadastroOS, Administrativo, TermoContrato, TermoAditivo,
 Demandante, TipoServico, Sistema)

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('login', 'senha',)

class CadastroOSForm(forms.ModelForm):

    processo_adm = forms.ModelChoiceField(queryset=Administrativo.objects.all(), widget=forms.Textarea())
    termo_contrato = forms.ModelChoiceField(queryset=TermoContrato.objects.all(), widget=forms.Textarea())
    termo_contrato_aditivo = forms.ModelChoiceField(queryset=TermoAditivo.objects.all(), widget=forms.Textarea())
    demandante = forms.ModelChoiceField(queryset=Demandante.objects.all(), widget=forms.Textarea())
    tipo = forms.ModelChoiceField(queryset=TipoServico.objects.all(), widget=forms.Textarea())
    sistema = forms.ModelChoiceField(queryset=Sistema.objects.all(), widget=forms.Textarea())

    class Meta:
        model = CadastroOS
        fields = ('mes_fatura','responsavel', 'prioridade','data_necessidade', 'solicitacao', 'esforco_estimado', 
        'esforco_realizado', 'esforco_relacionamento', 'data_entrega', 'data_aceite', 'mes_fatura',
        'ano_fatura', 'observacao')


   
  