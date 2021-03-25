from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("route1",views.route1,name="route1"),
    path("reserved",views.reserved, name="reserve"),
    path("<str:person>",views.greet,name="greet"),
    
]