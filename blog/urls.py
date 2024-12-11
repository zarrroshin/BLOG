from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    #path('detail/<slug:slug>', views.show, name='article_detail'),
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),

    # path('list',views.article_list,name='list'),
    path('list', views.ArticleListView.as_view(), name='list'),
    path('category/<slug:slug>', views.category_detail, name='category_list'),
    path('search/', views.search, name='search'),
    path('contact', views.MessageView.as_view(), name='contact'),
    path('users', views.UserList.as_view(), name='user_list'),


    # path('testbase',views.TestBaseView.as_view(),name='test_base'),
    path('red', views.HomePageRedirect.as_view(), name='redirect'),
    path('messages', views.MessageListView.as_view(), name='message_list'),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('archive', views.ArchiveIndexArticleView.as_view(), name='archive'),

]
