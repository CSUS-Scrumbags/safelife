from django import forms
from administrator.models import Course

class CourseNotesUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('notes',)