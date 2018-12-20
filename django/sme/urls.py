
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
