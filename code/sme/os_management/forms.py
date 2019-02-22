from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select
from .models import (MeuLogin, CadastroOS, Administrativo, TermoContrato, TermoAditivo,
Demandante, TipoServico, Sistema, Fase, Status, EstimarEsforco)


class MeuLoginForm(forms.ModelForm):

    class Meta:
        model = MeuLogin
        fields = ('login', 'senha',)
        

class DateForm(forms.Form):

    date = forms.DateField(input_formats=['%d/%m/%Y'])


class CadastroOSForm(forms.ModelForm):

    DEMANDANTE = (
        (1, 'CIEDU/RH'),
        (2, 'CIEDU/ESCOLA ALUNOS'),
        (3, 'COGED/DIPAR'),
        (4, 'COGED/DIDEM'),
        (5, 'COGED/GAB'),
        (6, 'COAD/UNIFORME'),
        (7, 'COAD/GAB'),
        (8,'CODAE/GTIC'),
        (9,'CODAE/LEVE LEITE'),
        (10,'CODAE/PROGRAMAÇÃO'),
        (11,'CODAE/LOGISTICA'),
        (12,'COTIC/DISIS'),
        (13,'CODAE/ATENDIMENTO'),
        (14,'COGEP/DIDES'),
        (15,'COGEP/DICAR'),
        (16,'COTIC/DITEC'),
        (17,'CIEDU/ATENDIMENTO'),
        (18,'COGEP/GAB')
    )

    SISTEMA = (
        (1, 'EOL-CONVÊNIOS'),
        (2, 'EOL-ESCOLA ALUNOS'),
        (3, 'EOL-RH'),
        (4, 'EOL-TEG'),
        (5, 'EOL-UNIFORME'),
        (6, 'EOL-GEO'),
        (7, 'EOL-LEVE LEITE'),
        (8,'EOL-REFEIÇÕES SERVIDAS'),
        (9,'EOL-REFEIÇÕES SERVIDAS TERCEIRIZADAS'),
        (10,'EOL-CENSO'),
        (11,'EOL-GERENCIAMENTO PROJETO'),
        (12,'PAPA'),
        (13,'SISU'),
        (14,'ATENDIMENTO AO CIEDU'),
        (15,'ATENDIMENTO A COAD'),
        (16,'ATENDIMENTO A CODAE'),
        (17,'ATENDIMENTO A COGED'),
        (18,'ATENDIMENTO A COGEP'),
        (19, 'ATENDIMENTO A COTIC'),
        (20, 'PORTAL GERENCIAL'),
        (21, 'ATENDIMENTO A COPED'),
        (22, 'ATENDIMENTO A SME'),
        (23, 'EOL-EVOLUÇÃO FUNCIONAL'),
        (24, 'SUPORTE A INFRAESTRUTURA')
    )

    TIPO = (
        (1, 'CORREÇÃO'),
        (2, 'ADAPTAÇÃO'),
        (3, 'NOVA FUNCIONALIDADE'),
        (4, 'ANÁLISE'),
        (5, 'EXTRA PRODUÇÃO'),
        (6, 'EVOLUÇÃO'),
        (7, 'NOVO PROJETO'),
        (8,'SUPORTE'),
    )

    PA = (
        (1, '6016.2016/0015803-3'),
    )


    TC = (
        (1, '133/SME/2014'),

    )

    
    TAC = (
        (1, '91/SME/2017'),
        (2, '238/SME/2017'),
        (3, '54/SME/2018'),
        (4, '56/SME/2018'),


    )

    demandante = forms.ChoiceField(choices=DEMANDANTE)
    responsavel = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite o responsável por esta solicitação'}))
    tipo = forms.ChoiceField(choices=TIPO)
    sistema = forms.ChoiceField(choices=SISTEMA)
    processo_adm = forms.ChoiceField(choices=PA)
    termo_contrato = forms.ChoiceField(choices=TC)
    termo_contrato_aditivo = forms.ChoiceField(choices=TAC)
     


    class Meta:
        model = CadastroOS
        fields = ('demandante' ,'responsavel', 'processo_adm', 'termo_contrato', 'termo_contrato_aditivo','tipo', 'prioridade', 'sistema', 'solicitacao')
        widgets = {
            'solicitacao': Textarea(attrs={'cols': 20, 'rows': 5, 'placeholder':'Descreva qual foi a necessidade que gerou está solicitação'})
        }
    


class EstimarOSForm(forms.ModelForm):

    n_os = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Digite o numero da Ordem de Serviço'})) 
    
    class Meta:
        model = CadastroOS
        fields = ('n_os','data_entrega',)
   
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
       
    
