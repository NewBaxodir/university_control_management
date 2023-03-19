from django.urls import path
from educational_department import views 




# namespace='educational_department'
urlpatterns = [
    path('', views.home_uquv_management, name='home'),
    path('add/hr', views.add_hr_views, name='add_hr'),   
    path('add/cafedra', views.add_cafedra_view, name='add_cafedra'),
    path('add/faculty', views.add_faculty_view, name='add_faculty'),
]

