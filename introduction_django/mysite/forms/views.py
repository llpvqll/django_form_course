from django.shortcuts import render

# Create your views here.


def base(request):
    template = 'base.html'
    return render(request, template)