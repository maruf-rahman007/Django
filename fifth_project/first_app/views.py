from django.shortcuts import render
from django.http import HttpResponse
from . forms import contactForm
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'./first_app/about.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'./first_app/about.html')

def home(request):
    return render(request,'./first_app/home.html')

def form(request):
    return render(request,'./first_app/form.html')

def DjangoForm(request):
    form = contactForm()
    return render(request,'./first_app/django_form.html',{'form':form})