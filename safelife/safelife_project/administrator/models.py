from django.db import models
from datetime import datetime

# Create your models here.
class Class(models.Model):
    classID = models.CharField(max_length=10, primary_key = True)
    classDate1 = models.DateField(blank=False)
    classDate2 = models.DateField(blank=False)
    classDate3 = models.DateField(blank=False)
    classDate4 = models.DateField(blank=False)
    classDate5 = models.DateField(blank=False)
    classDate6 = models.DateField(blank=False)
    classDate7 = models.DateField(blank=False)
    classDate8 = models.DateField(blank=False)
    classDate9 = models.DateField(blank=False)
    classDate10 = models.DateField(blank=False)
    classDate11 = models.DateField(blank=False)
    classDate12 = models.DateField(blank=False)

class Meta:
        app_label="administrator"

