# Generated by Django 5.1.1 on 2024-10-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=255),
        ),
    ]
