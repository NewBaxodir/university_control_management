from django.shortcuts import render, redirect
from django.contrib.auth import login as login_func, logout as logout_func,authenticate
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest

from django.contrib.auth.models import Group

UQUV_MANAGEMENT = Group.objects.get(name='uquv_management')
FACULTY_MANAGEMENT = Group.objects.get(name='faculty_management')
KAFEDRA_MANAGEMENT = Group.objects.get(name='kafedra_management')


def login(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_func(request, user) 
            # O'quv bo'limi odami ekanligini tekshirish
            try:
                user.groups.get(pk=UQUV_MANAGEMENT.pk)
                return redirect('educational_department:home')
            except: pass
            
            # Dekanat odami ekanligini tekshirish
            try:
                user.groups.get(pk=FACULTY_MANAGEMENT.pk)
                return redirect('fakultet:faculty_dep_home')
            except: pass
            
            # Kafedra mudiri ekanligini tekshirish
            try:
                user.groups.get(pk=KAFEDRA_MANAGEMENT.pk)
                return redirect('cafedra:dep_home')
            except: pass

            logout_func(request)           
        else:
            messages.info(request, 'Login or password error')
    context = {}
    return render(request, 'login/login.html',context)


def logout(request: WSGIRequest):
    logout_func(request)
    return redirect('auth:login')