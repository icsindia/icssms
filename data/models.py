from django.db import models
from course.models import Subject

class Data(models.Model):
    invoiceno=models.CharField(max_length=5)
    date=models.DateField()
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    report=models.TextField(max_length=200)
    def __str__(self):
        return self.invoiceno


