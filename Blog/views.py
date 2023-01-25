from django.shortcuts import render
from App_blog.urls import *

def inicio(request):
    return render(request, "home.html")