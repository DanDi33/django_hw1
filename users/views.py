from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login

menu = []

def home(request):
    return render(request, "home.html", {'menu': menu, 'title': 'Главная страница'})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, 'invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)