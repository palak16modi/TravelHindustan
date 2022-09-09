from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',Home,name='home'),
    path('signup/',SignUpView.as_view(),name='signup'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dashbord'), name='logout'),
    
    
]

