from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'dsafasdfe34353'})


def about(request):
    return render(request, 'generator/about.html')


def password(requestk):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    password = ""
    length = int(request.GET.get('length'))
    for char in range(length):
        password += random.choice(characters)
    return render(request, 'generator/password.html', {"password": password})
