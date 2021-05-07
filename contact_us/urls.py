from django.urls import path
from .views import *

urlpatterns = [
    path('contact_us',Contact_us,name='contact_us'),
    ]