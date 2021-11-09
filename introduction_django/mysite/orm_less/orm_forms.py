from django.forms import ModelForm, Form
from django import forms
from .models import Human


class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'birth', 'company', 'salary']


