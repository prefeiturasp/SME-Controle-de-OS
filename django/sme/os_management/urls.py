from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('visualizarOS/', views.visualizarOS, name='visualizarOS'),
]