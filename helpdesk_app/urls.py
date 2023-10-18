from django.urls import path
from . import views

urlpatterns = [
    path('', views.unauthorized_user_form, name='main_page'),
    path('success/', views.success, name='success'),
    path('login/', views.user_login, name='employee_login'),
    path('problems/', views.problem_list, name='employee_ticket_list'),
    path('logout/', views.user_logout, name='user_ticket_submission'),
    path('specific/<int:problem_id>/', views.specific, name='specific_info'),
]

