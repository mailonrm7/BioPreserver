"""
URL configuration for config project.

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
from django.urls import path
from .views import BiomaView, QuizView, ResultadosView  # Importe as views necessárias
from django.urls import path, include  # Certifique-se de incluir o "include"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('resultados/', views.ResultadosView.as_view(), name='resultados'),
]

urlpatterns = [
    # Rota para a página de biomas
    path('biomas/', BiomaView.as_view(), name='biomas'),

    # Rota para a página de quiz
    path('quiz/', QuizView.as_view(), name='quiz'),

    # Rota para a página de resultados
    path('resultados/', ResultadosView.as_view(), name='resultados'),
]

