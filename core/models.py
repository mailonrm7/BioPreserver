from django.db import models

class Bioma(models.Model):
    nome = models.CharField(max_length=255)  # Nome do bioma
    descricao = models.TextField()  # Descrição do bioma
    imagem_url = models.URLField(max_length=200)  # URL da imagem

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.nome

class Question(models.Model):
    question_text = models.CharField(max_length=255)  # Texto da pergunta
    answer_1 = models.CharField(max_length=255)  # Alternativa 1
    answer_2 = models.CharField(max_length=255)  # Alternativa 2
    answer_3 = models.CharField(max_length=255)  # Alternativa 3
    correct_answer = models.CharField(max_length=255)  # Resposta correta

    def __str__(self):
        return self.question_text

# Create your models here.
