from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('visualizarOS/', views.visualizarOS, name='visualizarOS'),
    path('estimarOS/', views.estimarOS, name='estimarOS'),
    path('relat_emerg/', views.relat_emerg, name='relat_emerg'),
    path('relat_em_espera/', views.relat_em_espera, name='relat_em_espera'),
    path('relat_em_fatura/', views.relat_em_fatura, name='relat_em_fatura'),
    path('relat_em_atraso/', views.relat_em_atraso, name='relat_em_atraso'),
    path('aprovarOS/', views.aprovarOS, name='aprovarOS'),

]

