from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


def log(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('none')
            # Return an 'invalid login' error message.
    return render(request, 'account/login.html')



def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    context = {'errors':[]}
    if request.method == 'POST':
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        if password != password2:
            context['errors'].append("Passwords must match")
            return render(request, 'account/register.html',context)
        if User.objects.filter(username=username):
            context['errors'].append("Username already taken")
            return render(request, 'account/register.html',context)

        if username and email and password:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return redirect('/')


    return render(request,'account/register.html')

