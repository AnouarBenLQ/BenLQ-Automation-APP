from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
    
# Create your views here.

def CustomLogoutView(request):
    
    request.session.flush()
    logout(request)
    return redirect('accounts:login')

@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class IndexView(TemplateView):
    template_name = 'accounts/home.html'

@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'accounts/userprofile.html'
   
    
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    def form_valid(self, form):
        # Your logic for a successful login
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Form is not valid, display errors
        messages.error(self.request,form.errors)
        
        return super().form_invalid(form)

