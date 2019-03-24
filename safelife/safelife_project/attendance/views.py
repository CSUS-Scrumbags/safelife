from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from administrator.models import Student
from django.db import connection
import datetime


def index(request):
    # Get the current date in the following format: <4 Digit Year>-<2 Digit Month>-<2 Digit Day>
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get the name of each student that is enrolled in the class
    all_students = Student.objects.select_related().raw('SELECT * '
                                                        'FROM students as S, classes as CL, attendances as A '
                                                        'WHERE CL.course_id = "301" AND S.student_id = A.students '
                                                        'AND CL.course_id = A.classes AND CL.date = A.date '
                                                        'AND A.date = %s ', [currentdate])
    # Get every recorded absence prior to the current date
    absent_students = Student.objects.select_related().raw('SELECT * '
                                                           'FROM students as S, classes as CL, attendances as A '
                                                           'WHERE CL.course_id = "301" AND S.student_id = A.students '
                                                           'AND CL.course_id = A.classes AND CL.date = A.date '
                                                           'AND A.status = "Absent" AND A.date < %s', [currentdate])
    # Create a template using index.html, and pass into it the list of student names and recorded absences 
    template = loader.get_template('index.html')
    context = {
        'all_students': all_students,
        'absent_students': absent_students
    }
    
    # Render the template to the user
    return HttpResponse(template.render(context, request))


def update_student(request):
    # Get the current date in the following format: <4 Digit Year>-<2 Digit Month>-<2 Digit Day>
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get the student name that was passed from the web page
    name = request.GET['studentName']
    # Get the Student_ID from the Student table
    student_data = Student.objects.get(student_name=name)
    # Create a cursor to execute raw SQL queries.
    with connection.cursor() as cursor:
        # Get the students attendance status
        cursor.execute('SELECT A.status ' 
                       'FROM students as S, classes as CL, attendances as A '
                       'WHERE CL.course_id = "301" AND S.student_id = A.students '
                       'AND CL.course_id = A.classes AND CL.date = A.date '
                       'AND A.date = %s AND S.student_name = %s', [currentdate, student_data.student_name])
        # attendance_status is a tuple containing the students attendance status
        attendance_status = cursor.fetchone()
    # Create a cursor to execute raw SQL queries.
    with connection.cursor() as cursor:
        # If the student was inadvertently marked as present, switch their status to Absent
        if attendance_status[0] == 'Present':
            cursor.execute('UPDATE attendances '
                           'SET status = "Absent" '
                           'WHERE students = %s AND date = %s', [student_data.student_id, currentdate])
        # If the students status is set to Absent, mark them Present
        else:
            cursor.execute('UPDATE attendances '
                           'SET status = "Present" '
                           'WHERE students = %s AND date = %s', [student_data.student_id, currentdate])
    # Render the response to the user
    return render(request, 'index.html', {})


def update_student_absent(request):
    # Get the current date in the following format: <4 Digit Year>-<2 Digit Month>-<2 Digit Day>
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    # Get the student name that was passed from the web page
    name = request.GET['studentName']
    # Get the absent date that was passed from the web page
    date = request.GET['absentDate']
    # Convert the date to the following format: <4 Digit Year>-<2 Digit Month>-<2 Digit Day>
    date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
    # Get the Student_ID from the Student table
    student_data = Student.objects.get(student_name=name)
    # Create a cursor to execute raw SQL queries.
    with connection.cursor() as cursor:
        # Get the students attendance status
        cursor.execute('SELECT A.status ' 
                       'FROM students as S, classes as CL, attendances as A '
                       'WHERE CL.course_id = "301" AND S.student_id = A.students '
                       'AND CL.course_id = A.classes AND CL.date = A.date '
                       'AND A.date = %s AND S.student_name = %s', [date, student_data.student_name])
        # attendance_status is a tuple containing the students attendance status
        attendance_status = cursor.fetchone()
    # Create a cursor to execute raw SQL queries.
    with connection.cursor() as cursor:
        if attendance_status[0] == 'Absent':
            # Change the students attendance status from Absent to 'Makeup: <date>'
            cursor.execute('UPDATE attendances '
                           'SET status = "Makeup: " %s'
                           'WHERE students = %s AND date = %s', [currentdate, student_data.student_id, date])
        else:
            # Change the students attendance status from 'Makeup: <date>' to Absent
            cursor.execute('UPDATE attendances '
                           'SET status = "Absent" '
                           'WHERE students = %s AND date = %s', [student_data.student_id, date])
    # Render the response to the user
    return render(request, 'index.html', {})

