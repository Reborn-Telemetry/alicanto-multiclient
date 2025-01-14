from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Ingresaste correctamente')
            return redirect('pages/bus-profile')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'login.html')

    # Manejo de solicitudes GET
    return render(request, 'login.html')

# Create your views here.
