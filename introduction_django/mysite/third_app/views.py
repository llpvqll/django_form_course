from django.shortcuts import render
import random

# Create your views here.


def index(request):
    template = 'third_app/index.html'
    return render(request, template)


def batman(request):
    template = 'third_app/batman.html'
    return render(request, template)


def joker(request):
    template = 'third_app/joker.html'
    return render(request, template)


def batman_car(request):
    template = 'third_app/batman_car.html'
    return render(request, template)

