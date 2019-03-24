from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^updateStudent/', views.update_student, name='update_student'),
    url(r'^updateStudentAbsent/', views.update_student_absent, name='update_student_absent'),
]
