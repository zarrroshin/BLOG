from tkinter.font import names

from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login',views.log,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('register',views.user_register,name='register'),
]