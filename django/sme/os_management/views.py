from django.shortcuts import render

def login(request):
    return render(request, 'os_management/login.html', {})
