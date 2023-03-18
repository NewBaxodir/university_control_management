from django.shortcuts import render, redirect
from django.contrib.auth import login as login_func, logout as logout_func,authenticate
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.





def login(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_func(request, user)
            return redirect('educational_department:home')
        else:
            messages.info(request, 'Login or password error')
    context = {}
    return render(request, 'login/login.html',context)


def logout(request: WSGIRequest):
    logout_func(request)
    return redirect('auth:login')