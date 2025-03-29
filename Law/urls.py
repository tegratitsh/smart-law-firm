from django.urls import path
from django.contrib.auth import views as auth_views
from .import views



urlpatterns = [
    path('', views.law_home_view, name='law-home'),
    path('area/', views.law_area_view, name='law-area'),
    path('law-contact/', views.law_contact_view, name='law-contact'),
    path('law-team/', views.law_team_view, name='law-team'),
    path('law-about/', views.law_about_view, name='law-about'),



    path('law-area-detail/<int:area_id>/', views.law_area_detail_view, name='law-area-detail'),
    path('law-title-detail/<int:title_id>/', views.law_title_detail_view, name='law-title-detail'),
    path('law-case/', views.law_case_view, name='law-case'),
    path('law-meeting/', views.law_meeting_view, name='law-meeting'),
    path('law-folder/', views.law_folder_view, name='law-folder'),
    path('law-folder-management/', views.law_folder_management_view, name='law-folder-management'),
    path('law-contact-management/', views.law_contact_management_view, name='law-contact-management'), 



    path('law-user-signup/', views.law_user_signup_view, name='law-user-signup'),
    path('law-user-login/', views.law_user_login_view, name='law-user-login'),

    path('law-user-logout/', views.law_user_logout_view, name='law-user-logout'),


    
    path('law-user-login/', auth_views.LoginView.as_view(template_name='Law/law_user_login.html'), name='law-user-login'),
    path('law-user-logout/', auth_views.LogoutView.as_view(), name='law-user-logout'),


    path('law-file-manager/', views.law_file_manager_view, name='law-file-manager'),
    path('law-edit-area/<int:area_id>/', views.law_edit_area_view, name='law-edit-area'),
    path('law-edit-title/<int:title_id>/', views.law_edit_title_view, name='law-edit-title'),
    path('law-edit-service/<int:service_id>/', views.law_edit_service_view, name='law-edit-service')
   ]

