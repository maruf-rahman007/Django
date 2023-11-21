from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request,"home.html", {'data': student})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll)
    print(std)
    student = models.Student.objects.all()
    return render(request,"home.html", {'data': student})