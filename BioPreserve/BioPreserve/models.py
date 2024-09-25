from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.email
class Bioma(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
class Quiz(models.Model):
    pergunta = models.CharField(max_length=255)
    bioma = models.ForeignKey(Bioma, on_delete=models.CASCADE)
    dificuldade = models.IntegerField()

    def __str__(self):
        return self.pergunta
class ResultadoQuiz(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    acertos = models.IntegerField()
    erros = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.email} - {self.quiz.pergunta}'


# Create your models here.
