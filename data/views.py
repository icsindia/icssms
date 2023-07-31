from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DataForm
from .models import Fees, Student

def index(request):
    if request.method=='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data saved submitted successfully.')
    form=DataForm()
    context = {
        "form":form
        }
    return render(request,"index.html",context)
def fees(request):
    if request.method=='POST':
        feesdate=request.POST['date']
        fees=Fees.objects.filter(duedate=feesdate)
        context = {
        "fees":fees
        }
        return render(request,"fees.html", context)
    return render(request,"fees.html")
def start(request):
    if request.method == 'POST':
        invoiceno=request.POST['invoiceno']
        student=Student.objects.get(invoiceno=invoiceno)
        return render(request, "start.html",{'student':student})
    return render(request, "start.html")
