# from django.http import HttpResponse
from django.shortcuts import render
from .models import Quiz, Riddle, Option


def home(request):
	context = {
		'quizes': Quiz.objects.all()
	}
	return render(request, 'quiz/home.html', context)


def rules(request):
	return render(request, 'quiz/rules.html', {'title': 'Rules'})


def about(request):
	return render(request, 'quiz/about.html', {'title': 'About'})


def enigma(request):
	context = {
		'enigmas': Riddle.objects.all(),
		'options': Option.objects.all(),
		'title': 'Enigma'
	}
	return render(request, 'quiz/enigma.html', context)
