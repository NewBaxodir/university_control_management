from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from moderator.models import MainUser

from educational_department.models import EducationalDepartmentManager
from fakultet.models import FacultyManager, Faculty
from cafedra.models import CafedraManager, Cafedra

from study_plan.models import (
    Direction,
    ProfessionalPractice,
    Science,
    ScienceStudyPlan,
    SemestrStudyPlan,
)


# admin.site.register(Group)
# admin.site.register(Group, GroupAdmin)



class MainUserAdmin(UserAdmin):
    ''' Asosoy userlari '''
    list_display = ['username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']
admin.site.register(MainUser, MainUserAdmin)




class EducationalDepartmentManagerAdmin(admin.ModelAdmin):
    ''' O'quv bo'limi '''
    list_display = ['user', 'pk']
admin.site.register(EducationalDepartmentManager, EducationalDepartmentManagerAdmin)



class FacultyManagerAdmin(admin.ModelAdmin):
    ''' faultet menegerlari '''
    list_display = ['user', 'pk']
admin.site.register(FacultyManager, FacultyManagerAdmin)



class CafedraManagerAdmin(admin.ModelAdmin):
    ''' kafedra managerlari '''
    list_display = ['user', 'pk']
admin.site.register(CafedraManager, CafedraManagerAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'id']
admin.site.register(Faculty, FacultyAdmin)



class CafedraAdmin(admin.ModelAdmin):
    list_display = ['name','faculty' ,'manager']
admin.site.register(Cafedra, CafedraAdmin)



class ScienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'cafedra', 'id']
admin.site.register(Science, ScienceAdmin)



class DirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'language', 'study_form', 'code', 'year', 'semester_number']
admin.site.register(Direction, DirectionAdmin)



class SemestrStudyPlanAdmin(admin.ModelAdmin):
    list_display = ['direction', 'semester_number']
admin.site.register(SemestrStudyPlan, SemestrStudyPlanAdmin)


class ScienceStudyPlanAdmin(admin.ModelAdmin):
    list_display = ['semestr_plan', 'science', 'science_code', 'exam_type', 'credit', 'course_work']
admin.site.register(ScienceStudyPlan, ScienceStudyPlanAdmin)


class ProfessionalPracticeAdmin(admin.ModelAdmin):
    list_display = ['semestr_plan', 'time']
admin.site.register(ProfessionalPractice, ProfessionalPracticeAdmin)