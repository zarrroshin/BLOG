from django.urls import path

from . import views

app_name = "blog"
urlpatterns =[
    path('detail/<slug:slug>', views.show,name='article_detail'),
    #path('list',views.article_list,name='list'),
    path('list',views.ArticleListView.as_view(),name='list'),
    path('category/<slug:slug>', views.category_detail,name='category_list'),
    path('search/',views.search,name='search'),
    path('contact',views.contactus,name='contact'),

    path('users',views.UserList.as_view(),name='user_list'),
    #path('testbase',views.TestBaseView.as_view(),name='test_base'),
]