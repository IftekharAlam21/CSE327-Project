from django.shortcuts import render
from django.views.generic import CreateView
from .models import Person

# Create your views here.
class UserCreateView(CreateView):
    model = Person
    template_name =  'signup/login.html'
    fields = ('name', 'email', 'password')
