from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  #default route, 
    path("arzoo", views.arzoo, name="arzoo"),
    path("<str:name>", views.greet, name="greet")
]