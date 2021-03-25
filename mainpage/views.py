from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"mainpage/index.html")

def route1(request):
    return HttpResponse("A different Landing Page!")

def greet(request,person):
    return render(request,"mainpage/greet.html",{"name":person.capitalize()})

def reserved(req):
    return HttpResponse("This Page is reserved!")
