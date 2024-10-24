"""
URL configuration for biopreserve project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import redirect
from core import views  # Importe as views corretas

def login_view(request):
    # Autenticação bem-sucedida
    return redirect('home')  # Certifique-se de que a URL com nome 'home' está configurada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as URLs do app Core
     path('quiz/', views.quiz_view, name='quiz'),
    path('resultados/', views.resultados_view, name='resultados'),
    # Outras URLs...

    
]



