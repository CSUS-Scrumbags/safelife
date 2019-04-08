from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from administrator.models import Course, CourseTeacher

@login_required(login_url='/users')
def home(request):
        admin_current_courses = Course.objects.select_related().raw('SELECT * '
                                                        'FROM course_teachers as CT, courses as C '
                                                        'WHERE CT.teachers_id = %s AND C.course_id = CT.course_id', [request.user.id])
        template = loader.get_template('administrator/dashboard.html')
        context = {
        'admin_current_courses': admin_current_courses
        }
    
    # Render the template to the user
        return HttpResponse(template.render(context, request))


