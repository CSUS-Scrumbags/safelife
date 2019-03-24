from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from administrator.models import Student
from django.db import connection
import datetime


def index(request):

    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    all_students = Student.objects.select_related().raw('SELECT * '
                                                        'FROM students as S, classes as CL, attendances as A '
                                                        'WHERE CL.course_id = "301" AND S.student_id = A.students '
                                                        'AND CL.course_id = A.classes AND CL.date = A.date '
                                                        'AND A.date = %s ', [currentdate])
    absent_students = Student.objects.select_related().raw('SELECT * '
                                                           'FROM students as S, classes as CL, attendances as A '
                                                           'WHERE CL.course_id = "301" AND S.student_id = A.students '
                                                           'AND CL.course_id = A.classes AND CL.date = A.date '
                                                           'AND A.status = "Absent" AND A.date <= %s', [currentdate])

    template = loader.get_template('index.html')
    context = {
        'all_students': all_students,
        'absent_students': absent_students
    }
    return HttpResponse(template.render(context, request))


def update_student(request):
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    name = request.GET['studentName']
    student_data = Student.objects.get(student_name=name)
    with connection.cursor() as cursor:
        cursor.execute('SELECT A.status ' 
                       'FROM students as S, classes as CL, attendances as A '
                       'WHERE CL.course_id = "301" AND S.student_id = A.students '
                       'AND CL.course_id = A.classes AND CL.date = A.date '
                       'AND A.date = %s AND S.student_name = %s', [currentdate, student_data.student_name])
        attendance_status = cursor.fetchone()
    print(attendance_status[0])
    print(student_data.student_id)

    with connection.cursor() as cursor:
        if attendance_status[0] == 'Present':
            cursor.execute('UPDATE attendances '
                           'SET status = "Absent" '
                           'WHERE students = %s AND date = %s', [student_data.student_id, currentdate])
            print("Updated to Absent!")
        else:
            cursor.execute('UPDATE attendances '
                           'SET status = "Present" '
                           'WHERE students = %s AND date = %s', [student_data.student_id, currentdate])
            print("Updated to Present!")
    return render(request, 'index.html', {})


def update_student_absent(request):
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    name = request.GET['studentName']
    date = request.GET['absentDate']
    date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
    print(name)
    print(date)
    student_data = Student.objects.get(student_name=name)

    with connection.cursor() as cursor:
        cursor.execute('UPDATE attendances '
                       'SET status = "Makeup: " %s'
                       'WHERE students = %s AND date = %s', [currentdate, student_data.student_id, date])

    return render(request, 'index.html', {})

