from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class MenuView(TemplateView):
    template_name = 'menu/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'menu/login.html'
