from django.db import models
from datetime import datetime
from administrator.models import Class

# Create your models here.
class attendance(models.Model):
    studentID = models.CharField(max_length=10)
    classID = models.ForeignKey(Class, on_delete=models.CASCADE)
    class1 = models.BooleanField(default=True)
    class2 = models.BooleanField(default=True)
    class3 = models.BooleanField(default=True)
    class4 = models.BooleanField(default=True)
    class5 = models.BooleanField(default=True)
    class6 = models.BooleanField(default=True)
    class7 = models.BooleanField(default=True)
    class8 = models.BooleanField(default=True)
    class9 = models.BooleanField(default=True)
    class10 = models.BooleanField(default=True)
    class11 = models.BooleanField(default=True)
    class12 = models.BooleanField(default=True)
    makeup1 = models.DateField(default=None, blank=True)
    makeup2 = models.DateField(default=None, blank=True)
    makeup3 = models.DateField(default=None, blank=True)
    makeup4 = models.DateField(default=None, blank=True)
    makeup5 = models.DateField(default=None, blank=True)
    makeup6 = models.DateField(default=None, blank=True)
    makeup7 = models.DateField(default=None, blank=True)
    makeup8 = models.DateField(default=None, blank=True)
    makeup9 = models.DateField(default=None, blank=True)
    makeup10 = models.DateField(default=None, blank=True)
    makeup11 = models.DateField(default=None, blank=True)
    makeup12 = models.DateField(default=None, blank=True)

class Meta:
        app_label="attendance"

