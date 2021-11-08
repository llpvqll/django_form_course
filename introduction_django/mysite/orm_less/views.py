from django.shortcuts import render
from .models import Human
# Create your views here.


def orm_base(request):
    template = 'orm_base.html'
    all_human = Human.objects.all()
    context = {
        'all_human': all_human,
    }
    return render(request, template, context)

