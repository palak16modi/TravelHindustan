from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/',Blogs,name='blogs'),
    
    ]