from django.urls import path
from educational_department import views 




# namespace='educational_department'
urlpatterns = [
    path('', views.home_uquv_management, name='home'),
    path('add/hr', views.add_hr_views, name='add_hr'),   
]

