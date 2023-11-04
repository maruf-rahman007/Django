from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'./first_app/index.html')

def home(request):
    return render(request,'./first_app/home.html')