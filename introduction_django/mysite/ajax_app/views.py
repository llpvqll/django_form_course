from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from .forms import UserCreateForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from orm_less.models import Human
from .forms import HumanForm
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


class MainView(TemplateView):
    template_name = 'ajax_index.html'
    human_form = HumanForm

    def get(self, request):
        context = {}
        context['script'] = 'alert(5555555);'

        if request.user.is_authenticated:
            all_humans = Human.objects.all()
            context['humans'] = all_humans
            context['human_form'] = self.human_form
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/ajax_app/login"
    template_name = "ajax_register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "ajax_login.html"
    success_url = "/ajax_app/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_valid(form)


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/ajax_app/')


def validate_email(request):
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data = {
                'is_taken': "This email already registered!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': "There were no registrations for this mailing address!"})


def show_all(request):
    all_elem = Human.objects.all().values()
    context = {
        'elements': list(all_elem)
    }
    return JsonResponse(context)


def close_all(request):
    close_elem = ""
    context = {
        'elements': list(close_elem)
    }


def add_human(request):
    if request.POST:
        if request.is_ajax():
            name = request.POST['name']
            surname = request.POST['surname']
            birth = request.POST['birth']
            company = request.POST['company']
            salary = request.POST['salary']
            human = Human.objects.create(name=name,
                                         surname=surname,
                                         birth=birth,
                                         company=company,
                                         salary=salary)
            return JsonResponse(human.dict())


