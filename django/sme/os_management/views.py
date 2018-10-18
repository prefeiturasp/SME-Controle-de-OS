
from django.shortcuts import render
from django.conf import settings
from .forms import LoginForm, CadastroOSForm
from .models import CadastroOS

def login(request):
    form = LoginForm
    return render(request, 'os_management/login.html', {'form': form})

def menu(request):
    return render(request, 'os_management/menu.html', {})

def cadastro(request):
    form = CadastroOSForm
    return render(request, 'os_management/cadastro.html', {'form': form})
