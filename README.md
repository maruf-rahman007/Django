# Django


# Django Installation
    1. First Create a Virtual Environment For Project it can be global or local . 
            pip install virtualenv
            virtualenv --version (check version)
    2. Name yout environment 
            virtualenv name
    3. This will give a sourse file which includes a Script and we need to actiate it 
            source ./my_env/Scripts/activate
    4. After this install Django
            pip install django
            python -m django --version (check version )
# Create Django project
    1. django-admin startproject first_project
    2. cd first_project
    3. python manage.py runserver To run the aplication

# Project Directory Stracture

    init.py : Python packages / all logical work 
    wsgi.py : Web server gateway / how the website will communicate with server
    asgi.py : it has both synchronous and synchronous behaviour 
    settings.py : All kind of settings
    urls.py : All the urls of project
    manage.py : command line utility 

# Working with URLS
    1. Create url  || path('',views.home),
    2. Hit url 
    3. views will return whatever it has 
        in Django everything we need to return we return it in HttpResponse. For this we need to import HttpResponse from django.http in views file

# Create App
    1. -> django-admin startapp app_name (command line)
    2. Go to settings.py and add it to the settings
    3. Go to urls.py and include it
        -> from django.urls import path,include
        -> path('first_app/', include('first_app.urls'))
    4. make urls.py in the app do the rest

# Nevigation 
    1. Look at second_project

# Rendering Template
    