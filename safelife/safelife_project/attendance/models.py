from django.db import models
from datetime import datetime
from student.models import student
from classes.models import classes

# Create your models here.
class attendance(models.Model):
    studentID = models.ForeignKey(student, on_delete=models.CASCADE)
    classID = models.CharField(max_length=10, primary_key = True)
    status = models.CharField(max_length=5)
    date = models.DateTimeField(default=datetime.now, blank=True)
