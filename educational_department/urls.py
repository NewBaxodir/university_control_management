from django.urls import path
from educational_department import views 


urlpatterns = [
    path('', views.home_uquv_management, name='home'),
]

