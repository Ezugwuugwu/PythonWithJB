from django.http import request
from django.shortcuts import render


# Create your views here.

def my_project(request):
    return render(request, 'my_project.html', {})
