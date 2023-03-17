from django.shortcuts import render

# Create your views here.




def dep_home(request):
    return render(request, 'cafedra/home.html')
