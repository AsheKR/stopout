from django.shortcuts import render

from school.models import School, Student


def student_list(request):
    slist = Student.objects.all()

    return render(request, 'school/student_list.html', {'student_list': slist})


def school_list(request):
    slist = School.objects.all()

    return render(request, 'school/school_list.html', {'school_list': slist})


def school_detail(request, pk):
    student_list = School.objects.get(pk=pk).student_set.all()

    return render(request, 'school/school_detail.html', {'student_list': student_list})


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    return render(request, 'school/student_detail.html', {'student': student})
