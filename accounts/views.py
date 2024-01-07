from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render, redirect
# Create your views here.
    
# Create your views here.
@method_decorator(login_required(login_url='login'), name='dispatch')
class IndexView(TemplateView):
    template_name = 'dashboard/home.html'
   
    
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    def form_valid(self, form):
        # Your logic for a successful login
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Form is not valid, display errors
        messages.error(self.request, f'Login failed. Error: {form.errors}')
        return super().form_invalid(form)