from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("ceci est la page index de jeux<br><a href='/'>go back</a>")
