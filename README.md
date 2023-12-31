# Django


## Django Installation
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
## Create Django project
    1. django-admin startproject first_project
    2. cd first_project
    3. python manage.py runserver To run the aplication

## Project Directory Stracture

    init.py : Python packages / all logical work 
    wsgi.py : Web server gateway / how the website will communicate with server
    asgi.py : it has both synchronous and synchronous behaviour 
    settings.py : All kind of settings
    urls.py : All the urls of project
    manage.py : command line utility 

## Working with URLS
    1. Create url  || path('',views.home),
    2. Hit url 
    3. views will return whatever it has 
        in Django everything we need to return we return it in HttpResponse. For this we need to import HttpResponse from django.http in views file

## Create App
    1. -> django-admin startapp app_name (command line)
    2. Go to settings.py and add it to the settings
    3. Go to urls.py and include it
        -> from django.urls import path,include
        -> path('first_app/', include('first_app.urls'))
    4. make urls.py in the app do the rest

## Nevigation 
    1. Look at second_project

## Rendering Template
    As Django follows MVT where T stands for template . So when we show any html file we actually render it for this 
    1. Make a templates file in root folder and inside it make html files
    2. Go to Views.py and import render from django.shortcuts
    3. We also need to let the settings know about this . For this go to setting.py -- TEMPLATES -- 'DIRS': [BASE_DIR/"templates"],
    4. From views.py return render (request,'html_filename')

## Static File 
    |---> Unchanged (image,css,video,audio,js)
    1. Make a static folder in the base directory
    2. add folders in that according to needs like css , image , js
    3. Django never let you use static file directly
        Settings.py
            |---> static url STATICFILES_DIRS =[
                                BASE_DIR / "static",
                           ]
    4. HTML (<img src="{% static 'image/pp.png' %}" alt="My pic">)
    5. {% load static %} ON TOP OF HTML FILE
    6. For app the processes are same just make sure files name are not the same 
        views.py path = (./first_app/indexx.html)
## Dynamic File / Media file
    |---> Changeable
    |---> Comes from backend
    1. Go to settings and add this MEDIA_ROOT = BASE_DIR/"media"
                                   MEDIA_URL = 'media/'
    
    2. Go to urls and add 
            from django.conf import settings
            from django.conf.urls.static import static
            + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

## Add Boostrap to Django
    1. Simple AF just add boostrap in tour template html 


## URL Tag 
    1. path('home/',views.home,name = "homepage"),
    2. href="{% url 'homepage' %}"

## Template Inheritance
    1. extends Tag
        * {% extends 'parent_template_name' %} IN CHILD File

    2. block Tag
        * {% block title %}....{% endblock %} / <title>{% block title %}{% endblock %}</title> in base.html

## Creating Custom Template and Template Tags
    1. Create a new folder in first app named templatetags


## HTML Forms in Django
    1. Use CSRF token
    2. Get / post request
    3. Action
    4. email = request.POST.get('email') using this we get the input value in views.py

## Django Build in Form api
    

# Django Models

##    Orm
        It's a Midium. Object Relation Mapping that helps application to interact with databases. Converts python code to mysql code.
        QuerySet can be defined as a list containing all those objects we have created using Django models. it helps us to 
            1. Read Data 
            2. Filter Data 
            3. Order Data

##    Model
        It is a source of information that holdes information of data and it's behaviour
        Each models denotes a table in database , Each attribute represents a database field.
        Django provides in build sqllite but we can use others if we need

##    Migrations
        It's basically a way of saying django to add those model changes 

                (makemigration)      (migrate)
        Model Class -------> SQL code -------> Exicute SQL 

        showmigrations shows the changes
        
    1. You will find models in every app inbuild just go there and create a class with necessary fields 
        ex : 
            class Student(models.Model):
            name = models.CharField(max_length=20)
            roll = models.IntegerField(primary_key=True)
            address = models.TextField()
    2. Then use the command 
        * python manage.py makemigrations (Create SQL DB)
        * python manage.py migrate (Run that)
    3. If you add any extra fiels after this you need to set a default value for that and then do the same commands

##    Admin / SuperUser

    1. python manage.py createsuperuser
    2. You need to let django know that you want to give access to admin for that perticular database and for this 
       go to first_app then admin.py and import models (from . import models)
       and then  admin.site.register(models.Student)
    3. To see by the name in the admin panel add a simple function __str__ in models.py
            def __str__(self):
                return self.name
    4. Go to views.py & 
        * from . import models
        * student = models.Student.objects.all()
    5. Pass this as dictionery
        * return render(request,"home.html", {'data': student})
    
    
