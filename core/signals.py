from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Question

@receiver(post_migrate)
def create_default_questions(sender, **kwargs):
    if sender.name == 'core':  # Verifica se é o aplicativo core
        if not Question.objects.exists():  # Verifica se já existem perguntas
            questions = [
                {
                    "question_text": "Qual é o maior bioma do Brasil?",
                    "answer_1": "Amazônia",
                    "answer_2": "Cerrado",
                    "answer_3": "Pantanal",
                    "correct_answer": "Amazônia"
                },
                {
                    "question_text": "O que caracteriza o bioma Cerrado?",
                    "answer_1": "Florestas tropicais",
                    "answer_2": "Savanas",
                    "answer_3": "Desertos",
                    "correct_answer": "Savanas"
                },
                {
                    "question_text": "Qual é um problema enfrentado pela Amazônia?",
                    "answer_1": "Desmatamento",
                    "answer_2": "Agricultura",
                    "answer_3": "Nenhuma",
                    "correct_answer": "Desmatamento"
                },
                {
                    "question_text": "O Pantanal é conhecido por sua:",
                    "answer_1": "Riqueza em fauna",
                    "answer_2": "Riqueza em flora",
                    "answer_3": "Grande deserto",
                    "correct_answer": "Riqueza em fauna"
                },
                {
                    "question_text": "O que significa 'biodiversidade'?",
                    "answer_1": "Variedade de vida",
                    "answer_2": "Número de espécies",
                    "answer_3": "Extinção",
                    "correct_answer": "Variedade de vida"
                },
            ]

            for q in questions:
                Question.objects.create(**q)
