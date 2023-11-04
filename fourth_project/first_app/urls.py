from django.urls import path,include
from . import views

urlpatterns = [
    path('about/',views.about,name = "aboutpage"),
    path('home/',views.home,name = "homepage"),
]