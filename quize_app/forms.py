from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Riddle


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']


class CreateQuestionForm(forms.ModelForm):
    quiz = forms.ModelChoiceField(queryset=Quiz.objects.all())

    class Meta:
        model = Riddle
        fields = ['quiz', 'text', 'answer']
