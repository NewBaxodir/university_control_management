from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, Http404


from educational_department.models import *
from .utils import get_educational_department_manager_or_404, custom_404, custom_template_name as _
from login.views import FACULTY_MANAGEMENT, KAFEDRA_MANAGEMENT, UQUV_MANAGEMENT


from fakultet.models import Faculty, FacultyManager
from cafedra.models import Cafedra, CafedraManager
from study_plan.models import Science, Direction


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from login.decorators import unauthenticated_user , allowed_users, admin_only


@login_required(login_url='auth:login')
@admin_only
def home_uquv_management(request):
    return render(request, _('home'), {
        'id': 0,
    })


# Human resource qo'shish
@login_required(login_url='auth:login')
def add_hr_views(request: WSGIRequest):
    error_msg = ''
    LIST_SELECT = ['k_m', 'f_d', 'o_d']
    if request.method == 'POST':
        username =      request.POST.get('username', False)
        first_name =    request.POST.get('first_name', False)
        last_name =     request.POST.get('last_name', False)
        email =         request.POST.get('email', False)
        password =      request.POST.get('password_1', False)
        password_2 =    request.POST.get('password_2', False)
        hr_s =          request.POST.get('hr_s', False)
        try:
            MainUser.objects.get(username=username)
            error_msg = 'Bunday foydalanuvchi nomi mavjud. Iltimos boshqa foydalanuvchi nomini kiriting !'
        except:
            if username and first_name and last_name and email \
                and password and password_2 and hr_s in LIST_SELECT and password_2 == password:
                user = MainUser.objects.create(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.is_active = True
                user.is_staff = True
                user.save()
                if hr_s == 'k_m':
                    user.groups.add(KAFEDRA_MANAGEMENT)
                    CafedraManager.objects.create(user=user)

                if hr_s == 'f_d':
                    user.groups.add(FACULTY_MANAGEMENT)
                    FacultyManager.objects.create(user=user)

                if hr_s == 'o_b': 
                    user.groups.add(UQUV_MANAGEMENT)
                    EducationalDepartmentManager.objects.create(user=user)

                user.save()
                return redirect('educational_department:home')
            else:
                error_msg = 'Ma\'lumotlar noto\'g\'ri kiritilgan !'
    return render(request, _('add_hr'), {
        'error_msg': error_msg,
        'id': 1,
    })



def add_cafedra_view(request: WSGIRequest):
    managers = CafedraManager.objects.filter(is_manager = False)
    facultys = Faculty.objects.all()
    error_msg = ''
    if request.method == 'POST':
        cafedra_name = request.POST.get('cafedra_name', False)
        faculty = request.POST.get('faculty', False)
        manager = request.POST.get('manager', False)

        try:
            manager = CafedraManager.objects.get(user__username=manager)
        except:
            error_msg = 'Kafedra managerini tanlang'
        
        try:
            faculty = Faculty.objects.get(id=faculty)
        except:
            error_msg = 'Fakultetni tanlang'
        
        if cafedra_name and faculty and manager and not error_msg:
            Cafedra.objects.create(
                name=cafedra_name,
                manager=manager,
                faculty=faculty,
            )
            manager.is_manager = True
            manager.save()
            return redirect('educational_department:home')
        else:
            error_msg = 'Barcha bandlarni to\'ldiring '
        

    return render(request, _('add_cafedra'), {
        'id': 1,
        'managers': managers,
        'facultys': facultys,
        'error_msg': error_msg,
    })



def add_faculty_view(request: WSGIRequest):
    managers = FacultyManager.objects.filter(is_manager=False)
    error_msg = ''
    if request.method == 'POST':
        manager = request.POST.get('manager', False)
        faculty = request.POST.get('faculty_name', False)

        try:
            manager = FacultyManager.objects.get(user__username=manager)
        except:
            manager = False
            error_msg = 'Mas\'ul shaxsni tanlang'
        
        try:
            faculty = Faculty.objects.get(name=faculty)
            error_msg = 'Ushbu nomdagi fakultet avvaldanoq mavjud. Iltimos boshqa nom kiriting'
        except:
            pass
        
        if manager and faculty and not error_msg:
            Faculty.objects.create(
                name=faculty,
                manager=manager,
            )
            manager.is_manager = True
            manager.save()
            return redirect('educational_department:home')
        else:
            print(manager, faculty, error_msg)

    return render(request, _('add_fakultet'), {
        'id': 1,
        'managers': managers,
    })







































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