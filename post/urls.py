from . import views
from django.urls import include

from django.urls import path


urlpatterns = [
    
    path("post/", views.post_detail, name="post_detail"),
]