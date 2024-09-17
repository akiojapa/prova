from django.db import models
from django import forms


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Computador(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    data = models.IntegerField()

    def __str__(self):
        return self.nome


class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = ['nome', 'cor', 'data']

class Periferico(models.Model):
    nome = models.CharField(max_length=100)
    computador = models.ForeignKey(Computador, on_delete=models.CASCADE)

class PerifericoForm(forms.ModelForm):
    class Meta:
        model = Periferico
        fields = ['nome', 'computador']
