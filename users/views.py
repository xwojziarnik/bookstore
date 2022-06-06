from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")
