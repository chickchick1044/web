from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all().order_by('-id')
    context = {
        'students': students,
    }
    return render(request, 'students/index.html', context)

def new(request):
    return render(request, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    student = Student.objects.create(name=name, age=age)
    return redirect(f'/students/{student.pk}/')

def detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,
    }
    return render(request, 'students/detail.html', context)

def delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/students/')

def edit(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,
    }
    return render(request, 'students/edit.html', context)

def update(request, pk):
    student = Student.objects.get(id=pk)
    name = request.POST.get('name')
    age = request.POST.get('age')

    student.name = name
    student.age = age
    student.save()

    return redirect(f'/students/{student.pk}/')


