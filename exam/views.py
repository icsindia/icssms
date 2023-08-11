from django.shortcuts import render
from django.http import HttpResponse
def exam(request):
    return render(request,"exam.html")
