from django.shortcuts import render
from django.http import HttpResponse
from data.models import Student, Fees
from exam.models import ExamStudent, Exam
def exam(request):
    return render(request,"exam.html")
def addstudent(request):
    examlist=Exam.objects.all()
    context={
        "exam":examlist
    }
    if request.method=='POST':
        invoiceno=request.POST['invoiceno']
        name=request.POST['name']
        phone=request.POST['phone']
        course=request.POST['course']
        examid=request.POST['examid']
        examlink=request.POST['examlink']
        dateofexam=request.POST['examdate']
        examtime=request.POST['examtime']
        ex=ExamStudent.objects.create(invoiceno=invoiceno,name=name,phone=phone,course=course,examid=examid, examlink=examlink,dateofexam=dateofexam,examtime=examtime)
    return render(request,"addstudent.html", context)
def getexam(request):
    if request.method=='GET':
        invoiceno=request.GET['invoiceno']
        student=Student.objects.filter(invoiceno=invoiceno)
        exam=ExamStudent.objects.filter(invoiceno=invoiceno)
        context={
            "student":student,
            "exam":exam
        }
        return render(request,"getexam.html",context)
def getexamid(request):
    if request.method=='GET':
        examid=request.GET['examid']
        getexamdata=Exam.objects.filter(examid=examid)
        context={
            "getexamdata":getexamdata
        }
        return render(request,"getexamid.html",context)
def getexamdata(request):
    if request.method=='GET':
        invoiceno=request.GET['invoiceno']
        data=ExamStudent.objects.filter(invoiceno=invoiceno)
        data1=ExamStudent.objects.filter(invoiceno=invoiceno).first()
        context = {
            "data":data,
            "data1":data1
        }
    return render(request,"getexamdata.html",context)
def examlist(request):
    list=ExamStudent.objects.all()
    context={
        "list":list
    }
    return render(request, "examlist.html",context)
