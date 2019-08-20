from django.shortcuts import render
from bookwormsnsu.models import User
# Create your views here.

def index(request):
    return render(request,'bookwormsnsu/index.html')
