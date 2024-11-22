from django.shortcuts import render,get_object_or_404
from blog.models import Article
# Create your views here.
def show(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return  render(request, 'blog/article-details.html', context={'article':article})


def article_list(request):
    articles = Article.objects.all()
    return render(request,'blog/article_list.html', context={'articles':articles})