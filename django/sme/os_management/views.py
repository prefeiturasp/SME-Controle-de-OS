from django.shortcuts import render, redirect
from django.conf import settings
from .forms import (MeuLoginForm, CadastroOSForm, EstimarOSForm)
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required (login_url='/accounts/login/')
def meulogin(request):
    template_name = 'accounts/meuLogin.html'
    if request.method == 'POST':
        form = MeuLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(settings.LOGIN_URL)
    else:
        form = MeuLoginForm() 
    context = {
        'form': form
    }   
    return render(request, template_name, context)

@login_required
def menu(request):
    if not request.user.is_authenticated:
       return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request, 'os_management/menu.html', {})

@login_required
def cadastro(request):
    form = CadastroOSForm
    return render(request, 'os_management/cadastro.html', {'form': form})

@login_required
def estimarOS(request):
    form = EstimarOSForm
    if not request.user.has_perm('global_permissions.acesso_estima_os_config'):
        raise PermissionDenied
    else:
        return render(request, 'os_management/estimarOS.html', {'form': form})

@login_required
def relatorios(request):
    return render(request, 'os_management/relatorios.html', {})
    
@login_required
def visualizarOS(request):
    return render(request, 'os_management/visualizarOS.html', {})
    

@login_required
def Relat_emerg(request):
    return render(request,'relat_emerg.html', {})
    

@login_required
def Relat_em_espera(request):
    return render(request,'relat_em_espera.html', {})

@login_required
def Relat_em_fatura(request):
    return render(request,'relat_fatura.html', {})

@login_required
def Relat_em_atraso(request):
    return render(request,'relat_em_atraso.html', {})
    
    