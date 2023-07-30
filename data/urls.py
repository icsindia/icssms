from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("fees/", views.fees, name="fees"),
    path("start/", views.start, name="start"),
]