from django.shortcuts import render, redirect

from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')

    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    # 저장 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(title=title, content=content)
    context = {
        'article' : article
    }
    # return render(request, 'articles/create.html', context)
    return redirect('/articles/')