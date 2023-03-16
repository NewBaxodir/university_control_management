from educational_department.models import EducationalDepartmentManager
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings
from django.http import Http404, HttpResponse
from django.db.models import Q


def custom_404(request: WSGIRequest = None, get_text: bool = False):
    ERROR_CODE = '''
<!doctype html>
<html lang="en">
    <head>
        <title>Not Found</title>
    </head>
    <body>
        <h1> Not Found </h1>
        <p> The requested resource was not found on this server.</p>
    </body>
</html> '''
    if get_text:
        return ERROR_CODE
    if settings.DEBUG:
        raise Http404()
    else:
        raise Http404(ERROR_CODE)

def get_educational_department_manager_or_404(request: WSGIRequest):
    ''' Foydalanuvchining o'quv bo'limi manageri ekanligini aniqlaydigan qism dastur '''
    user = request.user
    if not user.is_authenticated:
        custom_404(request)
    if not user.is_active and user.is_staff:
        custom_404(request)
    try:
        return EducationalDepartmentManager.objects.get(user_id=user.id)
    except:
        custom_404(request)


def custom_template_name(name: str):
    return 'educational_department/%s.html'%(name)

