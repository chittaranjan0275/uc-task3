import logging

from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Student, Teacher


def index(request):
    students = Student.objects.using('studentdb').all()
    teachers = Teacher.objects.using('teacherdb').all()
    for student in students:
        print('Name of student: ',student.name, ' Roll NO: ',student.roll_no,' Mobile NO: ',student.mob_number)

    for teacher in teachers:
        print('Name of teacher: ', teacher.name, ' Department: ', teacher.department, ' Mobile NO: ', teacher.mob_number)
    return render(request, 'index.html')
