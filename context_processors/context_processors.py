


def recent_articles(request):
    from blog.models import Article, Category
    recent_articles = Article.objects.order_by('-created')
    categories = Category.objects.all()
    return  {'recent_articles': recent_articles,'categories': categories}


