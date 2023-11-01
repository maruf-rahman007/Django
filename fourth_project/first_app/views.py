from django.http import HttpResponse

def about(request):
    return HttpResponse('''<h1>About Page </h1> ''')