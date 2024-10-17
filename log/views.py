from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages



def login_page(request):
  if request.user.is_authenticated:
    return redirect('bus-profile')
  
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    try:
            user = User.objects.get(username=username)
    except:
            messages.error(request, 'El usuario no existe')

    user = authenticate(request, username=username, password=password)

    if user is not None:
            login(request, user)
            messages.success(request, 'Ingresaste correctamente')
            return redirect('bus-profile')
    else:
            messages.error(request, 'nombre de usuario o contraseña incorrectos')

# Create your views here.
