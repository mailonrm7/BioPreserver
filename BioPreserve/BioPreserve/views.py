from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Bioma, Quiz, ResultadoQuiz
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class BiomaView(TemplateView):
    template_name = 'biomas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biomas'] = Bioma.objects.all()
        return context

class QuizView(TemplateView):
    template_name = 'quiz.html'

class ResultadosView(View):
    def get(self, request):
        return render(request, 'resultados.html')


# Create your views here.
