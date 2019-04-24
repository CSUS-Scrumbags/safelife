from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reports/', views.report, name ='reports'),
    path('', views.index, name='index'),
    path('', views.report, name='teacher-reporting'),
    #path('<int:course_id>/', views.index, name='reports'),
    #path('success/', views.success, name = 'success'),   
]