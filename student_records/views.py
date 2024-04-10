from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        student = Student(name=name, marks=marks)
        student.save()
        return redirect('home')
    return render(request, 'add_student.html')

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home')
