from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-id') #=> QuerySet ~= List
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request): # POST를 받음
    # GET(URL을 통해 데이터를 전달 받음), POST(http body를 통해 데이터를 전달받음)
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.create(title=title, content=content)
    # article.title
    # article.content

    return redirect(f'/articles/{article.pk}/')

def detail(request, pk): # pk: primary key
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return  render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()
    
    return  redirect(f'/articles/{article.pk}/')
    