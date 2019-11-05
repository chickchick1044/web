from django.shortcuts import render, redirect
from .models import Student, Comment

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
    # 1. pk에 해당하는 student를 db에서 가져오기
    student = Student.objects.get(id=pk)
    # 1-1. student의 comment를 다 가져오기
    comments = student.comment_set.all()
    # 1-2. student의 comment 개수 
    # comments.count

    context = {
        'student': student,
        'comments': comments,
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

def comments_new(request, student_pk):
    # 1. request에서 데이터 가져오기
    content = request.POST.get('content')
    # 2. Comment 생성
    comment = Comment()
    comment.content = content
    comment.student_id = student_pk
    comment.save()
    # 3. student 상세 페이지로 redirect
    return redirect('students:detail', student_pk)

# POST 요청을 받음
def comments_delete(request, student_pk, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('students:detail', student_pk)

def comments_edit(request, student_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        # POST
        # 1. POST로 넘어온 데이터 가져오기
        content = request.POST.get('content')
        # 2. comment에 바꿔 넣기 & 저장
        comment.content = content
        comment.save()
        # 3. 댓글목록 페이지로 redirect
        return redirect('students:detail', student_pk)

    else:
        # GET
        context = {
            'comment': comment,
        }
        return render(request, 'students/comments_edit.html', context)
