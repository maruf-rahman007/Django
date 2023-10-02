from django.http import HttpResponse

def home(request):
    return HttpResponse("This is My Home Page by maruf!")