from django.shortcuts import render
from .models import Human
from . import orm_forms
from django.views.generic import TemplateView
# Create your views here.


def orm_base(request):
    template = 'orm_base.html'
    all_humans = Human.objects.all()
    form_for_human = orm_forms.HumanForm
    form = orm_forms.HumanForm(request.POST)

    context = {
        'form_for_human': form_for_human,
        'all_humans': all_humans,
    }
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
    return render(request, template, context)


def delete_user(request):
    temp = 'delete.html'
    query = request.POST['delete']
    deleted_user = Human.objects.filter(pk=query).delete()
    context = {
        'query': query,
        'deleted_user': deleted_user
    }

    return render(request, temp, context)

