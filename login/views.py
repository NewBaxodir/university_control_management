from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
# Create your views here.





def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_uquv_management')
        else:
            messages.info(request, 'Login or password error')
    context = {}
    return render(request, 'login/login.html',context)