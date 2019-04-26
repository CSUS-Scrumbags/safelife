from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from administrator.models import Student, Class
from administrator.models import Course
from administrator.models import CourseStudent
from django.db import connection
import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users')
def index(request):

    current_user = request.user.id

    # Get the list of the current teacher courses
    teacher_current_courses = Course.objects.select_related().raw('SELECT * '
                                                        'FROM course_teachers as CT, courses as C '
                                                        'WHERE CT.teachers_id = %s AND C.course_id = CT.course_id AND C.is_complete = 0 ', [current_user])
    # Get the current date in the following format: <4 Digit Year>-<2 Digit Month>-<2 Digit Day>
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get the name of each student that is enrolled in the class



    all_courses = Course.objects.select_related().raw('SELECT *'
                                                        'FROM courses')
                                                        
    test = CourseStudent.objects.select_related().raw('SELECT *'
                                                        'FROM course_students')

    all_students = Student.objects.select_related().raw('SELECT * '
                                                            'FROM students as S, classes as CL, attendances as A '
                                                            'WHERE CL.course_id = 306 AND S.student_id = A.students '
                                                            'AND CL.course_id = A.classes AND CL.date = A.date '
                                                            )
                                                                                                           

    with connection.cursor() as cursor:
        cursor.execute('SELECT CS.course_id, S.student_name '
                       ' FROM course_students as CS, students as S, course_teachers as CT '
                       'WHERE CT.teachers_id = 1 AND CT.course_id = 306 AND CS.course_id = CT.course_id AND CS.students_id = S.student_id ')
        #all_students = cursor.fetchall()  
        #print(all_students) 
        cursor.execute('SELECT * '
                       'FROM courses')
        course_name = cursor.fetchone()

    with connection.cursor() as cursor:
                cursor.execute('SELECT CL.course_id, CL.date '
                                'FROM classes as CL, course_teachers as CT '
                                'WHERE CT.teachers_id = %s AND CL.date >= %s '
                                'AND CT.course_id = CL.course_id '
                                'GROUP BY CL.course_id ', [current_user, currentdate])
    
                next_class_date = cursor.fetchall()
    
    with connection.cursor() as cursor:
                cursor.execute('SELECT CS.course_id, COUNT(CS.students_id) '
                        'FROM course_teachers as CT, course_students as CS '
                        'WHERE CT.teachers_id = %s AND CT.course_id = CS.course_id '
                        'GROUP BY CS.course_id ', [current_user])
                teacher_student_count = cursor.fetchall()
        
                                                       

    # Create a template using index.html, and pass into it the list of student names and recorded absences 
    template = loader.get_template('index.html')
    context = {
        'all_courses': all_courses,
        'all_students': all_students,
        'test': test,
        'course_name': course_name,
        'next_class_date': next_class_date,
        'teacher_student_count': teacher_student_count,
        'teacher_current_courses': teacher_current_courses


    }
    
    # Render the template to the user
    return HttpResponse(template.render(context, request))



def report(request):

    class_dates = Class.objects.filter(course=301)


    #Get all the students in the class
    
    all_students = Student.objects.select_related().raw('SELECT * '
                                                            'FROM students as S, classes as CL, attendances as A '
                                                            'WHERE CL.course_id = 301 AND S.student_id = A.students '
                                                            'AND CL.course_id = A.classes AND CL.date = A.date '
                                                            'GROUP BY student_name'
                                                             )
    status = Student.objects.select_related().raw('SELECT   A.*'
                                                            'FROM students as S, classes as CL, attendances as A '
                                                            'WHERE CL.course_id = 301 AND CL.course_id = A.classes '
                                                            'AND CL.date = A.date '
                                                            'GROUP BY A.id'
                                                            'ORDER BY A.students'
                                                            )                                                                                                                 

    all_dates = Course.objects.select_related().raw('SELECT date '
                                                      'FROM classes, courses as C '
                                                      'WHERE C.course_id = 306 ')
    template = loader.get_template('reports.html')
    context = {
        'all_dates': all_dates,
        'class_dates': class_dates,
        'all_students': all_students,
        'status': status
        


    }
    
    # Render the template to the user
    return render(request, "reports.html", context)


