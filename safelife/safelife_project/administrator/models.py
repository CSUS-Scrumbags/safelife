from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=5, primary_key=True)
    student_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'students'


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=5, primary_key=True)
    teacher_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'teachers'


class Course(models.Model):
    course_id = models.CharField(max_length=5, primary_key=True)
    course_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'courses'


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_students'


class CourseTeacher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_teachers'


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        db_table = 'classes'


class Attendance(models.Model):
    students = models.CharField(max_length=5)
    classes = models.CharField(max_length=5)
    status = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        db_table = 'attendances'
