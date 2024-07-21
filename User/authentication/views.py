from django.urls import reverse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from User.models import User
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = User
    fields = ["username", 'password']
    template_name = 'register.html'


class UserLoginView(LoginView):
    template_name = 'login.html'  
    redirect_authenticated_user = True  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['your_custom_context'] = 'value'  # add any custom context data here
        return context
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('index'))


def log_out(request):
    logout(request)
    return redirect('index')


