from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def Home(request):
    return render(request,"users/minor_project.html",{})
 
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

