from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='quize-home'),
    path('rules', views.rules, name='quize-rules'),
    path('about', views.about, name='quize-about'),
    path('enigma', views.enigma, name='quize-enigma'),
]   