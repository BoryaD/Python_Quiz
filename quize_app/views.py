# from django.http import HttpResponse
from django.shortcuts import render
from .models import Quize, Enigma, Option

def home(request):
	context = {
		'quizes' : Quize.objects.all()	 
	}
	return render(request,'quize/home.html', context)

def rules(request):
	return render(request,'quize/rules.html',{'title':'Rules'})

def about(request):
	return render(request,'quize/about.html',{'title':'About'})

def enigma(request):
	context = {
		'enigmas' : Enigma.objects.all(),
		'options' : Option.objects.all(),
		'title':'Enigma'
	}
	return render(request,'quize/enigma.html',context)