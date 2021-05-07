from django.shortcuts import render
from .views import UserForm
from django.urls import path,include


urlpatterns = [
    path('rating/', UserForm, name='rating'),
]