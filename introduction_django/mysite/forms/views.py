from django.shortcuts import render, HttpResponse
from . import forms
# Create your views here.


def base(request):
    template = 'base.html'
    form_for_human = forms.HumanForm
    context = {
        'form_for_human': form_for_human
    }
    return render(request, template, context)


def add_user(request):
    form = forms.HumanForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
    return HttpResponse(f'New user was added! {request.path}')




