from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import (MeuLogin, CadastroOS, Administrativo, TermoContrato, TermoAditivo,
Demandante, TipoServico, Sistema, Fase, Status, EstimarEsforco)


class MeuLoginForm(forms.ModelForm):

    class Meta:
        model = MeuLogin
        fields = ('login', 'senha',)

class CadastroOSForm(forms.ModelForm):

    n_os = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Digite o numero da Ordem de Serviço'}))
    data_necessidade = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Digite a data que esta OSs deve ser entregue'}))
    data_necessidade = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Digite a data que esta OSs deve ser entregue'}))
    demandante = forms.ModelChoiceField(queryset=Demandante.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Digite a sua coordenadoria'}))
    responsavel = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite o responsável por esta solicitação'}))
    tipo = forms.ModelChoiceField(queryset=TipoServico.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Ex: Reparação, manutenção, nova funcionalidade'}))
    sistema = forms.ModelChoiceField(queryset=Sistema.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Ex: EOL, SGP, SERAP'}))
    processo_adm = forms.ModelChoiceField(queryset=Administrativo.objects.all(), widget=forms.TextInput())
    termo_contrato = forms.ModelChoiceField(queryset=TermoContrato.objects.all(), widget=forms.TextInput())
    termo_contrato_aditivo= forms.ModelChoiceField(queryset=TermoAditivo.objects.all(), widget=forms.TextInput())


    class Meta:
        model = CadastroOS
        fields = ( 'n_os','data_necessidade','demandante' ,'responsavel', 'processo_adm', 'termo_contrato', 'termo_contrato_aditivo','tipo', 'prioridade', 'sistema', 'solicitacao', 'observacao')
        widgets = {
            'solicitacao': Textarea(attrs={'cols': 20, 'rows': 5, 'placeholder':'Descreva qual foi a necessidade que gerou está solicitação'}),
            'observacao' : Textarea(attrs={'cols': 20, 'rows': 5}),
        }
    

class EstimarOSForm(forms.ModelForm):

    n_os = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Digite o numero da Ordem de Serviço'})) 
    fase = forms.ModelChoiceField(queryset=Fase.objects.all(), widget=forms.TextInput(attrs={'placeholder': 'Ex: Em andamento'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), widget=forms.TextInput())

    class Meta:
        model = CadastroOS
        fields = ('n_os','data_aceite','data_entrega',)
   
class VisualizarOSForm(forms.ModelForm):
    
    n_os = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Digite o numero da OS para visualizar o conteúdo'}))
    processo_adm = forms.ModelChoiceField(queryset=Administrativo.objects.all(), widget=forms.TextInput())
    termo_contrato = forms.ModelChoiceField(queryset=TermoContrato.objects.all(), widget=forms.TextInput())
    demandante = forms.ModelChoiceField(queryset=Demandante.objects.all(), widget=forms.TextInput())
    tipo = forms.ModelChoiceField(queryset=TipoServico.objects.all(), widget=forms.TextInput())
    sistema = forms.ModelChoiceField(queryset=Sistema.objects.all(), widget=forms.TextInput())

    class Meta:
        model = CadastroOS

        fields = ('n_os', 'processo_adm', 'termo_contrato' ,'data_aceite', 'demandante', 'responsavel', 'prioridade', 'tipo', 'sistema', 'data_necessidade','solicitacao', 'data_entrega',)
        widgets = {
            'solicitacao': Textarea(attrs={'cols': 20, 'rows': 5}),
        }



class RelatoriosForm(forms.ModelForm):

    class Meta:
        model = CadastroOS
        fields = ('n_os', 'data_aceite','data_necessidade', 'data_entrega')
       
    

    
