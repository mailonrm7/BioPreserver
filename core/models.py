from django.db import models

class Bioma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=100)
    answer_2 = models.CharField(max_length=100)
    answer_3 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

# Create your models here.
