from django.shortcuts import render
from . import urls
# Create your views here.

def contact(request):
    return render(request,'./first_app/index.html',{'Courses' : [
        {
            'id': 1,
            'courses':'C',
            'teacher':'Rahim'
         
        },
        {
            'id': 2,
            'courses':'C++',
            'teacher':'Rakib'
         
        },
        {
            'id': 3,
            'courses':'Python',
            'teacher':'Shakib'
         
        },
        {
            'id': 4,
            'courses':'SQL',
            'teacher':'Nakib'
         
        },
        {
            'id': 5,
            'courses':'DJANGO',
            'teacher':'Fakib'
         
        },
        ]})