from django.shortcuts import render, redirect
from blog.models import Article
from django.urls import reverse
# Create your views here
def home(request):
    article = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    return render(request,'home/index.html',context={'articles':article,'recent_articles':recent_articles})
