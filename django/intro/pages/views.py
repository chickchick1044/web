from django.shortcuts import render
import random
from datetime import datetime 

# Create your views here.
def index(request):
    context = {
        'name': 'nwith',
    }
    return render(request, 'pages/index.html', context)

def dinner(request):
    foods = ['초밥', '카레', '칼국수']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'pages/dinner.html', context)

# Variable Routing
def hello(request, name): #path('hello/<str:name>/', 와 같아야 함
    context = {
        'name': name,
    }
    return render(request, 'pages/hello.html', context)

# 실습
# 1. '이름'과 '나이'를 Variable Routing을 통해 받아서 자기소개
def hi(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/hi.html', context)

# 2. 숫자 2개를 Variable Routing을 통해 받아 곱셈 결과 보여주기
def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'pages/times.html', context)

def dtl(request):
    foods = ['짜장면', '짬뽕', '라면', '냉면']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'foods': foods,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/dtl.html', context)

# 실습
# Is it your birthday?
# 오늘이 자신의 생일이면 '예'를, 아니면 '아니오'를 보여주는 페이지
def birthday(request):
    today = datetime.now()
    result = (today.month==9 and today.day==25)
    
    context = {
        'today': today,
        'result': result,
    }
    return render(request, 'pages/birthday.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def generate(request):
    count = int(request.GET.get('count'))

    lotto_numbers = range(1, 46)
    my_lottos = []
    for n in range(count):
        sorted_lotto = sorted( random.sample(lotto_numbers, 6) )
        my_lottos.append(sorted_lotto)

    context = {
        'my_lottos': my_lottos,
        'count': count,
    }

    return render(request, 'pages/generate.html', context)

# GET vs POST
# GET - html 파일을 주세요 (return render)
# POST - 어떠한 일을 처리해주세요! ( 처리 했습니다 or 다른 페이지 리턴)
#      - 새로운 글을 써주세요! 글을 삭제해주세요!

def article_new(request):
    return render(request, 'pages/article_new.html')

def article_create(request):
    # request.GET #-> {'title': '제목', 'content': '내용' }
    title = request.POST.get('title') #-> 제목
    content = request.POST.get('content')  # -> 내용
    context = {
        'title': title,
        'content': content,
    }
    return render(request, 'pages/article_create.html', context)

# Static Files
# Image, CSS, HTML 통틀어 이야기하는 자원 or 파일
# html 파일과 같은 폴더에 넣고, 
# {% load static %}
def static_example(request):
    return render(request, 'pages/static_example.html')
