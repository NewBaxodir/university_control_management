from django.urls import path
from educational_department import views 


urlpatterns = [
    path('edu_dep/', views.home_uquv_management, name='home'),
    
]

