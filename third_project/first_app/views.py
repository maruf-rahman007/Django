from django.shortcuts import render
from . import urls
# Create your views here.

def contact(request):
    return render(request,'./first_app/indexx.html')