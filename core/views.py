import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Question
from .models import Bioma
# Página inicial
def home(request):
    return render(request, 'home.html')

# Página de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Página de cadastro
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Página de logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Página de biomas
@login_required
def biomas_view(request):
    # Recupera todos os biomas
    biomas = Bioma.objects.all()
    return render(request, 'biomas.html', {'biomas': biomas})

# Página de quizzes
@login_required
def quiz_view(request):
    return render(request, 'quiz.html')

# Página de resultados
@login_required
def resultados_view(request):
    return render(request, 'resultados.html')  # Simplesmente renderiza a página de resultados

#Página de quiz
@login_required

def quiz_view(request):
    # Recupera todas as perguntas do banco de dados
    questions = list(Question.objects.all())

    # Embaralha as perguntas aleatoriamente
    random.shuffle(questions)

    # Define o número máximo de perguntas a serem exibidas
    max_questions = 5
    questions = questions[:max_questions]

    if request.method == 'POST':
        score = 0  # Inicializa o placar de acertos

        # Processa as respostas enviadas pelo usuário
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')  # Obtém a resposta do usuário
            if user_answer == question.correct_answer:  # Verifica se a resposta está correta
                score += 1  # Incrementa o placar em caso de resposta correta

        # Renderiza a página de resultados com o score e o total de perguntas
        return render(request, 'resultados.html', {'score': score, 'total': max_questions})

    # Renderiza o template do quiz com as perguntas
    return render(request, 'quiz.html', {'questions': questions})