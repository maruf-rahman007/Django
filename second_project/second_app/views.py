from django.shortcuts import render

from django.http import HttpResponse

def courses(request):
    return HttpResponse('''
                        
                        <h1>This is Courses page</h1>
                        <a href = '/second_app/feedback/'>Feedback</a>
                        <br>
                        <a href = '/first_app/about/'>About</a>
                        <br>
                        <a href = '/first_app/contact/'>Contact</a>
                        
                        ''')
def feedback(request):
    return HttpResponse('''
                        
                        <h1>This is Feedback page</h1>
                        <a href = '/second_app/courses/'>Courses</a>
                        <br>
                        <a href = '/first_app/about/'>About</a>
                        <br>
                        <a href = '/first_app/contact/'>Contact</a>
                        
                        ''')

