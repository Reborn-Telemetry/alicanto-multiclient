from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path("diccionario-fusi/", views.dic_fusi, name='dic_fusi'),
  
]