from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home,name = "homepage"),
    path('about/',views.about,name = "aboutpage"),
    path('form/',views.form,name = "submit_form"),
    path('django_form/',views.DjangoForm,name = "django_form")
]