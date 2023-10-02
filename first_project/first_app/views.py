from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
   return HttpResponse("Hi there tell me your name")
def about(request):
    return HttpResponse("I'm a Student Learning DJANGO")