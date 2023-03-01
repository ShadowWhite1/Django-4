from django.shortcuts import render

from .models import Student


def students_list(request):
    template = '/Users/eldarrizaev/Desktop/orm_migrations/templates/school/students_list.html'

    students = Student.objects.all().prefetch_related('teacher').order_by('group')

    context = {'object_list': students}

    return render(request, template, context)
