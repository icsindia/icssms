from django.urls import path
from . import views

urlpatterns = [
    path("", views.exam, name="exam"),
    path("addstudent", views.addstudent, name="addstudent"),
    path('getexam/', views.getexam, name="getexam"),
    path('getexamid/', views.getexamid, name="getexamid"),
    path('getexamdata/', views.getexamdata, name="getexamdata"),
    path('examlist/', views.examlist, name="examlist"),
]