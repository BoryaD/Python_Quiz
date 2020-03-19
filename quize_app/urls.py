from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='quiz-home'),
    path('rules', views.rules, name='quiz-rules'),
    path('about', views.about, name='quiz-about'),
    path('enigma', views.enigma, name='quiz-enigma'),
]