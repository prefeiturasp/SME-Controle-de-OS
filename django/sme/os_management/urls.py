from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('visualizarOS/', views.visualizarOS, name='visualizarOS'),
    path('estimarOS/', views.estimarOS, name='estimarOS'),
]