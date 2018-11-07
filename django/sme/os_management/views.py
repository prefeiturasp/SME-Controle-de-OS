from django.shortcuts import render, redirect
from django.conf import settings
from .forms import (LoginForm, CadastroOSForm, EstimarOSForm)
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
        return redirect('/menu')
    else:
        form = LoginForm()
    return render(request, 'os_management/login.html', {'form': form})

def menu(request):
    return render(request, 'os_management/menu.html', {})

def cadastro(request):
    form = CadastroOSForm
    return render(request, 'os_management/cadastro.html', {'form': form})

def estimarOS(request):
    form = EstimarOSForm
    return render(request, 'os_management/estimarOS.html', {'form': form})

def relatorios(request):
    return render(request, 'os_management/relatorios.html', {})
    

def visualizarOS(request):
    return render(request, 'os_management/visualizarOS.html', {})
    