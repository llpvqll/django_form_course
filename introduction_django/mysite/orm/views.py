from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    template = 'base.html'
    return render(request, template)

