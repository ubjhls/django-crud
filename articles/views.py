from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Article
@require_POST

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')

    context = {
        'articles' : articles
    }
    
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request,'articles/new.html')

def create(request):
    if request.method == 'POST':
        # 저장 로직
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        # context = {
        #     'article' : article
        # }
        # return render(request, 'articles/create.html', context)
        
        return redirect('articles:detail', article.pk)
    else:
        return render(request,'articles/new.html')
        
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article' : article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(f'/articles/{article.pk}/')
    else:
        context = {
            'article' : article
        }
        return render(request, 'articles/edit.html', context)