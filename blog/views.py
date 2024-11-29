from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Article, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessagesForm
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic import ListView, DetailView


# Create your views here.
def show(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST['body']
        parent = request.POST['parent_id']
        user = request.user
        Comment.objects.create(body=body, user=user, article=article, parent_id=parent)
    return render(request, 'blog/article_detail.html', context={'article': article})


# def article_list(request):
#     articles = Article.objects.all()
#     paginator = Paginator(articles, 1)
#     page = request.GET.get('page')
#     object_list = paginator.get_page(page)
#     return render(request,'blog/article_list.html', context={'articles':object_list})
#


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    return render(request, 'blog/article_list.html', context={'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    return render(request, 'blog/article_list.html', context={'articles': object_list})


def contactus(request):
    if request.method == 'POST':
        form = MessagesForm(data=request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # email = form.cleaned_data['email']
            # text = form.cleaned_data['text']
            # Message.objects.create(title=title,email=email,text=text)

            # instance = form.save(commit=False) if you want to make some changes and then save the instance

            form.save()
    else:
        form = MessagesForm()
    return render(request, 'blog/contact.html', {'form': form})


# class TestBaseView(View):
#     name = "zarr"
#     def get(self, request):
#         return HttpResponse(self.name)
#
#
#
# class HelloToName(TestBaseView):


# class ListView(View):
#     queryset = None
#     template_name = None
#
#     def get(self, request):
#         return render(request, self.template_name, context={'object_list': self.queryset})


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'blog/article_list.html'

    def get(self, request):
        articles = self.queryset
        paginator = Paginator(articles, 1)
        page = request.GET.get('page')
        object_list = paginator.get_page(page)
        return render(request, self.template_name, context={'articles': object_list})


class UserList(ListView):
    queryset = User.objects.all()
    template_name = 'blog/user_list.html'


# class ArticleListView(TemplateView):
#     template_name = 'blog/article_list.html'
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_list'] = Article.objects.all()
#         return context


class HomePageRedirect(RedirectView):
    # url = "/"
    pattern_name = 'blog:list'
    permanent = False
    query_string = True
    def get_redirect_url(self,*args, **kwargs):
        print(self.request.user.username)
        return super().get_redirect_url(*args,**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    #template_name = "blog/article_detailll.html default=model_detail
    #context_object_name = 'article'
    #slug_field = 'slug'
    #slug_url_kwarg = 'item_slug'
    # queryset = Article.objects.filter(published=True)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name']="amirhossein"
    #     return context