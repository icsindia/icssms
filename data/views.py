from django.shortcuts import render
from .forms import DataForm

def index(request):
    form=DataForm()
    context = {
        "form":form
    }
    return render(request,"index.html",context)
