from django import forms
from django.forms import ModelForm, Textarea
from .models import (Login, CadastroOS, Administrativo, TermoContrato, TermoAditivo,
 Demandante, TipoServico, Sistema, Fase, Status)
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('login', 'senha',)
    
    def clean(self, *args, **kwargs):
         login = self.cleaned_data.get("login")
         senha = self.cleaned_data.get("senha")
         if login and senha:
            user = authenticate(username=login, password=senha)
            if not user:
               raise forms.ValidationError("Usuário não existe")
            if user.checkpassword(senha):
               raise forms.ValidationError("Senha inválida")
           


class CadastroOSForm(forms.ModelForm):

    demandante = forms.ModelChoiceField(queryset=Demandante.objects.all(), widget=forms.TextInput())
    tipo = forms.ModelChoiceField(queryset=TipoServico.objects.all(), widget=forms.TextInput())
    sistema = forms.ModelChoiceField(queryset=Sistema.objects.all(), widget=forms.TextInput())

    class Meta:
        model = CadastroOS
        fields = ( 'n_os','data_necessidade','demandante' ,'responsavel', 'tipo', 'prioridade', 'sistema', 'solicitacao', 'observacao')
        widgets = {
            'solicitacao': Textarea(attrs={'cols': 20, 'rows': 5}),
            'observacao' : Textarea(attrs={'cols': 20, 'rows': 5}),
        }
    

class EstimarOSForm(forms.ModelForm):

    processo_adm = forms.ModelChoiceField(queryset=Administrativo.objects.all(), widget=forms.TextInput())
    termo_contrato = forms.ModelChoiceField(queryset=TermoContrato.objects.all(), widget=forms.TextInput())
    termo_contrato_aditivo = forms.ModelChoiceField(queryset=TermoAditivo.objects.all(), widget=forms.TextInput())    
    fase = forms.ModelChoiceField(queryset=Fase.objects.all(), widget=forms.TextInput())
    status = forms.ModelChoiceField(queryset=Status.objects.all(), widget=forms.TextInput())
    
    class Meta:
        model = CadastroOS
        fields = ('n_os','data_entrega', 'processo_adm','mes_fatura', 'esforco_estimado', 
        'esforco_realizado', 'esforco_relacionamento', 'data_aceite', 'mes_fatura',
        'ano_fatura')
   