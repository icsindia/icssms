from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DataForm
from .models import Fees, Student, Data

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
        student=Student.objects.get(invoiceno=invoiceno.upper())
        data=Data.objects.filter(invoiceno=invoiceno.upper())
        context = {
            'student':student,
            'data':data
        }
        return render(request, "start.html",context)
    return render(request, "start.html")
def addfees(request):
    if request.method=='POST':
        invoiceno=request.POST['invoiceno']
        name=request.POST['name']
        batchtime=request.POST['batchtime']
        course=request.POST['course']
        fees=request.POST['fees']
        duedate=request.POST['duedate']
        ex=Fees.objects.create(invoiceno=invoiceno,name=name,batchtime=batchtime,course=course,fees=fees, duedate=duedate)
    return render(request, "addfees.html")
def getstudent(request):
    if request.method=='GET':
        invoiceno=request.GET['invoiceno']
        data=Student.objects.filter(invoiceno=invoiceno)
        context = {
            "data":data,
        }
    return render(request,"getstudent.html",context)
