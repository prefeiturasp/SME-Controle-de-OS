"""sme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('sme.os_management.urls')),
    path('menu/', include('sme.os_management.urls')),
    path('cadastro/', include('sme.os_management.urls')),
    path('visualizarOS/', include('sme.os_management.urls')),
    path('estimarOS/', include('sme.os_management.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('relat_emerg/', include('django.contrib.auth.urls')),
    path('relat_em_espera/', include('django.contrib.auth.urls')),
    path('relat_em_fatura/', include('django.contrib.auth.urls')),
    path('relat_em_atraso/', include('django.contrib.auth.urls')),
    path('aprovarOS/', include('sme.os_management.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
