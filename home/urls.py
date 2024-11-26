from django.urls import path

from account.urls import app_name
from home import views

app_name = 'home'
urlpatterns =[
    path("",views.home,name="home"),
    path("sidebar",views.sidbar,name="sidebar_partial"),
]