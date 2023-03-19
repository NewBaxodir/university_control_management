from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest

from educational_department.models import *
from .utils import get_educational_department_manager_or_404, custom_404, custom_template_name as _

from fakultet.models import Faculty, FacultyManager
from cafedra.models import Cafedra, CafedraManager
from study_plan.models import Science, Direction


from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from login.decorators import unauthenticated_user , allowed_users, admin_only


@login_required(login_url='auth:login')
@admin_only
def home_uquv_management(request):
    return render(request, _('home'), {})

@login_required(login_url='auth:login')
def add_hr_views(request: WSGIRequest):

    return render(request, _('add_hr'), {})















def all_faculty_view(request: WSGIRequest):
    facultys = Faculty.objects.all()

    return render(request, _('all_faculty'), {
        'id': 2,
        'page_name': ''' Fakultetlar ro'yxati ''',
        'data': facultys,
    })


def all_cafedra_view(request: WSGIRequest):
    cafedras = Cafedra.objects.all()

    return render(request, _('all_cafedra'), {
        'id': 3,
        'page_name': ''' Kafedralar ro'yxati ''',
        'data': cafedras,
    })


def all_direction_view(request: WSGIRequest):
    data = Direction.objects.all()
    facultys = Faculty.objects.all()
    main_search = request.GET.get('main_search', '')
    faculty_id = request.GET.get('faculty_id', '')
    language = request.GET.get('language', '')
    shape = request.GET.get('shape', '')
    year = request.GET.get('year', '')

    try:
        if main_search:
            data = data.filter(
                Q(name__contains=main_search) |
                Q(code__contains=main_search) |
                Q(faculty__name__contains=main_search)
            )
        if faculty_id:
            data = data.filter(faculty_id=faculty_id) 
        if language:
            data = data.filter(language=language)
        if shape:
            data = data.filter(study_form=shape)
        if year:
            data = data.filter(year=year)
    except:
        pass

    list_years = list(range(
        Direction.objects.all().order_by('year')[0].year, 
        Direction.objects.all().order_by('-year')[0].year + 1
    ))
    

    return render(request, _('directions'), {
        'id': 5,
        'page_name': ''' Yo'nalishlar ro'yxati ''',
        'data': data,
        'facultys': facultys,
        'list_years': list_years,
    })







 






















































































# 