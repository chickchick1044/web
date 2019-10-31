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
    if request.method == 'POST':
        # student를 생성(create)
        name = request.POST.get('name')
        age = request.POST.get('age')
        student = Student(name=name, age=age)
        student.save()
        return redirect('students:detail', student.pk)
    else: #=> 'GET'
        # new page를 보여줌
        return render(request, 'students/new.html')

# def create(request): => RESTful한 주소를 위해 new로 이동
#     name = request.POST.get('name')
#     age = request.POST.get('age')
#     student = Student.objects.create(name=name, age=age)
#     # return redirect(f'/students/{student.pk}/')
#     return redirect('students:detail', student.pk)

def detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,
    }
    return render(request, 'students/detail.html', context)

def delete(request, pk):
    if request.method == 'POST': # GET요청이 들어올 경우 수행x
        student = Student.objects.get(id=pk)
        student.delete()
        # return redirect('/students/')
        return redirect('students:index')

def edit(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':        
        student = Student.objects.get(id=pk)
        name = request.POST.get('name')
        age = request.POST.get('age')
        student.name = name
        student.age = age
        student.save()
        return redirect('students:detail', student.pk)

    else:
        context = {
            'student': student,
        }
        return render(request, 'students/edit.html', context)



# def update(request, pk):
#     student = Student.objects.get(id=pk)
#     name = request.POST.get('name')
#     age = request.POST.get('age')

#     student.name = name
#     student.age = age
#     student.save()
#     # return redirect(f'/students/{student.pk}/')
#     return redirect('students:detail', student.pk)


