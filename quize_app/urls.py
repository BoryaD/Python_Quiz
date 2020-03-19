from django.urls import path, re_path
from . import views
from .views import QuestionView, QuizListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', QuizListView.as_view(), name='quiz-home'),
    path('rules', views.rules, name='quiz-rules'),
    path('about', views.about, name='quiz-about'),
    re_path(r'^quiz/refresh/', views.quiz_refresh, name='quiz-refresh'),
    re_path(r'^quiz/check/', views.quiz_check, name='quiz-check'),
    re_path(r'^quiz/(?P<quiz_id>\d+)', QuestionView.as_view(), name='quiz-start'),
    re_path(r'^admin_question/$', views.admin_question, name='users-admin-question'),
    re_path(r'^admin_quiz/$', views.admin_quiz, name='users-admin-quiz'),

]
