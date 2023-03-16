from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('auth/logout', views.logout_view, name='logout'),
    path('faculty/', views.all_faculty_view, name='list_faculty'),
    path('cafedra/', views.all_cafedra_view, name='list_cafedra'),
    path('direction/', views.all_direction_view, name='list_direction'),
]

