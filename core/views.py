from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Question

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
    return render(request, 'biomas.html')

# Página de quizzes
@login_required
def quiz_view(request):
    return render(request, 'quiz.html')

# Página de resultados
@login_required
def resultados_view(request):
    return render(request, 'resultados.html')
#Página de quiz
@login_required
def quiz_view(request):
    if request.method == 'POST':
        # Obtendo as respostas do usuário
        score = 0
        questions = Question.objects.all()
        
        # Verifica se a resposta está correta
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1

        return render(request, 'resultados.html', {'score': score, 'total': questions.count()})

    # Renderizando as perguntas do quiz
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

# Create your views here.
