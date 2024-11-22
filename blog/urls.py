from django.urls import path

from . import views

app_name = "blog"
urlpatterns =[
    path('detail/<slug:slug>', views.show,name='article_detail'),
    path('list',views.article_list,name='list'),
]