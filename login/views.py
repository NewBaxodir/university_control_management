from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth import authenticate, login as dj_login
from django.shortcuts import redirect, render
from educational_department import views
# Create your views here.



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('educational_department:home_uquv_management')
        else:
            messages.info(request, 'Login or password error')
    context = {}
    return render(request, 'login/login.html',context)