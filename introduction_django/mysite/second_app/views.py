from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_of_404, render
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'second_app/index.html', context)


def detail(request, question_id):
    question = get_object_of_404(Question, pk=question_id)
    return render(request, 'second_app/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

