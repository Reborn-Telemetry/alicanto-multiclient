from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("simple_dashboard/", views.simple_dashboard, name='simple_dashboard'),
    path("no-access", views.no_access, name="no-access"),
]