from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1 style="color:red; font-size:50px; text-decoration:underline;">Welcome to Home</h1>')