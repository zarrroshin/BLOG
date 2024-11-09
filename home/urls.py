from django.urls import path

from account.urls import app_name
from home import views

app_name = 'home'
urlpatterns =[
    path("",views.home)
]