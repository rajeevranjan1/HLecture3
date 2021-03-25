import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request,"newyear/index.html",{"NY":now.month and now.day})


