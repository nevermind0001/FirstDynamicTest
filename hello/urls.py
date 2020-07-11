from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("daniele", views.daniele, name="daniele"),
    path("<str:name>", views.greet, name="greet")
]