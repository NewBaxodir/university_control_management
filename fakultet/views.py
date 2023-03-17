from django.shortcuts import render

# Create your views here.


def faculty_dep_home(request):
    return render(request, 'fakultet/home.html')
