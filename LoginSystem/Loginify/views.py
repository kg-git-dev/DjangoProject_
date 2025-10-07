from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def sign_up(request):
    return HttpResponse("Dummy link for sign up")

def log_in(request):
    return HttpResponse("Dummy link for log in")