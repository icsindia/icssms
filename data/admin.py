from django.contrib import admin
from .models import Data, Fees, Subject, Student, Course

class DataAdmin(admin.ModelAdmin):
    list_display=('invoiceno','date')
admin.site.register(Data,DataAdmin)
class FeesModel(admin.ModelAdmin):
    list_display=('invoiceno','duedate','fees','paiddate','paidamount')
admin.site.register(Fees,FeesModel)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Course)