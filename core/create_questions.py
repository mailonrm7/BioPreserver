from django.core.management.base import BaseCommand
from core.models import Question

class Command(BaseCommand):
    help = 'Cria perguntas padrão para o quiz'

    def handle(self, *args, **options):
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
            Question.objects.get_or_create(**q)

        self.stdout.write(self.style.SUCCESS('Perguntas criadas com sucesso.'))
