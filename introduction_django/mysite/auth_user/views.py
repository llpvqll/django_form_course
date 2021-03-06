from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.views.generic.base import View
from django.contrib.auth import logout
from orm_less.models import Human
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.


class IndexView(TemplateView):
    template_name = 'auth_user/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            context = {
                'humans': humans
            }
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/auth_user/login/"

    template_name = "auth_user/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "auth_user/login.html"

    success_url = "/auth_user/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/auth_user/")


