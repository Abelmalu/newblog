from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle



# Create your views here.
def artcile_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request,slug):
    article=Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html', {'article':article})

@login_required()
def artcile_create(request):
    if request.method=='POST':
        form = CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            #save article 
            return redirect('articles:list')

    else:   
        form = CreateArticle()
     
    return render(request,'articles/article_create.html',{'form':form})