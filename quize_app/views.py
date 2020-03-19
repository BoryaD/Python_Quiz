from datetime import datetime

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CreateQuizForm, CreateQuestionForm
from .models import Quiz, Riddle
from django.views.generic import ListView
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
import time


data_to_quizes = {}


def get_time_of_quiz(type_of_quiz):
    return data_to_quizes[type_of_quiz]['time_of_start']


def is_exist_quiz(type_of_quiz):
    return data_to_quizes.get(type_of_quiz)


def add_type_of_quiz(type_of_quiz, list_of_questions):
    if not data_to_quizes.get(type_of_quiz):
        data_to_quizes[type_of_quiz] = {'list_of_questions': list_of_questions, 'current_index': 0, 'time_of_start':
            time.time() * 1000}


def get_current_question(type_of_quiz):
    return data_to_quizes[type_of_quiz]['list_of_questions'][data_to_quizes[type_of_quiz]['current_index']]


def inc_question_index(type_of_quiz):
    data_to_quizes[type_of_quiz]['current_index'] += 1
    if len(data_to_quizes[type_of_quiz]['list_of_questions']) == data_to_quizes[type_of_quiz]['current_index']:
        data_to_quizes[type_of_quiz]['current_index'] = 0
    data_to_quizes[type_of_quiz]['time_of_start'] = time.time() * 1000


class QuestionView(ListView):
    model = Riddle
    template_name = 'quize/quiz.html'
    context_object_name = 'quiz'

    def dispatch(self, request, *args, **kwargs):
        self.answer_from_user = request.GET.get('answer')
        get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        if not is_exist_quiz(self.kwargs['quiz_id']):
            add_type_of_quiz(self.kwargs['quiz_id'], Riddle.objects.all().filter(quiz_id=self.kwargs['quiz_id']))
        return super(QuestionView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['is_answered'] = self.answer_from_user
        context['text'] = get_current_question(self.kwargs['quiz_id']).text
        context['cur_question'] = self.kwargs['quiz_id']
        return context


def home(request):
    context = {
        'quizes': Quiz.objects.all()
    }
    return render(request, 'quize/home.html', context)


class QuizListView(ListView):
    model = Quiz
    template_name = 'quize/home.html'
    context_object_name = 'quizes'
    paginate_by = 5


def rules(request):
    return render(request, 'quize/rules.html', {'title': 'Rules'})


def about(request):
    return render(request, 'quize/about.html', {'title': 'About'})


def quiz_refresh(request):
    type_of_quiz = request.GET.get('id')
    data = {
        'text': data_to_quizes[type_of_quiz]['list_of_questions'][data_to_quizes[type_of_quiz]['current_index']].text
    }
    quiz_index = request.GET.get('id')

    if int(request.GET.get('time')) - get_time_of_quiz(quiz_index) > 60000:
        inc_question_index(quiz_index)

    return JsonResponse(data)


def quiz_check(request):
    # Profile.objects.get(user_id=user_id).token
    print(request.GET)
    type_of_quiz = request.GET.get('id')
    answer = request.GET.get('answer')
    data = {
        'text': 'No'
    }

    if answer == get_current_question(type_of_quiz).answer:
        profile = Profile.objects.get(user_id=request.user.id)
        profile.token += 1
        profile.save()

        inc_question_index(type_of_quiz)
        data['text'] = "Yes it's correct"

    return JsonResponse(data)


def admin_question(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'New qestion has been updated!')
            return redirect('users-admin-question')

    else:
        form = CreateQuestionForm()

    context = {
        'form': form,
    }
    return render(request, 'quize/admin_question.html', context)



def admin_quiz(request):
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'New quiz has been updated!')
            return redirect('users-admin-quiz')

    else:
        form = CreateQuizForm()

    context = {
        'form': form,
    }
    return render(request, 'quize/admin_quiz.html', context)
