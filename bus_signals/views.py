from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def simple_dashboard(request):
    return render(request, 'simple_dashboard.html')

@login_required(login_url='login')
def no_access(request):
    return render(request, 'no-access.html')