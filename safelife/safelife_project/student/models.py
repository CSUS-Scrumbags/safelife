from django.db import models

class student(models.Model):
    studentID = models.CharField(max_length=10, primary_key = True)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
# Create your models here.
