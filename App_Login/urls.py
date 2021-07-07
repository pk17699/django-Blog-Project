from django.urls import path
from . import views

app_name = 'App_Login'
urlpatterns = [
    path('signup/', views.sign_up, name = 'signup'),
    path('signin/', views.login_page, name = 'signin'),
    path('logout/', views.logout_user, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('Change-profile/', views.user_change, name = 'user_change'),
    path('password/', views.pass_change, name = 'pass_change'),
    path('Change-Profile-Picture/', views.add_profile_pic, name = 'add_profile_pic'),
    path('Change-Picture/', views.change_profile_pic, name = 'change_profile_pic'),
]
