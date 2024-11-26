from django.shortcuts import render,get_object_or_404
from blog.models import Article, Category
from django.core.paginator import Paginator

# Create your views here.
def show(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return  render(request, 'blog/article-details.html', context={'article':article})


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    return render(request,'blog/article_list.html', context={'articles':object_list})



def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    articles= category.articles.all()
    return render(request,'blog/article_list.html', context={'articles':articles})