from django.shortcuts import render
from django.http import HttpResponse    
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def bootstrap_template(request):
    return render(request, 'template_bootstrap.html')

def data_diri(request):
    return render(request, 'data_diri.html')
