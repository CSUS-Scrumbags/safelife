from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from administrator.models import Student
from administrator.models import Course
from administrator.models import CourseStudent
from django.db import connection
import datetime


def index(request):
    # Get the current date in the following format: <4 Digit Year>-<2 Digit Month>-<2 Digit Day>
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get the name of each student that is enrolled in the class

    all_courses = Course.objects.select_related().raw('SELECT *'
                                                        'FROM courses')
                                                        
    test = CourseStudent.objects.select_related().raw('SELECT *'
                                                        'FROM course_students')                                               

    with connection.cursor() as cursor:
        cursor.execute('SELECT CS.course_id, S.student_name '
                       ' FROM course_students as CS, students as S, course_teachers as CT '
                       'WHERE CT.teachers_id = 1 AND CT.course_id = 306 AND CS.course_id = CT.course_id AND CS.students_id = S.student_id ')
        all_students = cursor.fetchall()  
        print(all_students)                                                

    # Create a template using index.html, and pass into it the list of student names and recorded absences 
    template = loader.get_template('index1.html')
    context = {
        'all_courses': all_courses,
        'all_students': all_students,
        'test': test

    }
    
    # Render the template to the user
    return HttpResponse(template.render(context, request))




