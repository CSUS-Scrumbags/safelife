from django.db import models

class classes(models.Model):
    classID = models.CharField(max_length=10, primary_key = True)
    teacher = models.CharField(max_length=30)
    class_Name = models.CharField(max_length=30)
    date = models.CharField(max_length = 10)