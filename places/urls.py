  
from django.urls import path
from .views import *

urlpatterns = [
    path('agra/',Agra,name='agra'),
    path('agra/hotels/',Hotels_Agra,name='hotels_agra'),
    path('jaipur/',Jaipur,name='jaipur'),
    path('jaipur/hotels/',Hotels_Jaipur,name='hotels_jaipur'),
    path('delhi/',Delhi,name='delhi'),
    path('delhi/hotels/',Hotels_Delhi,name='hotels_delhi'),
    path('shimla/',Shimla,name='shimla'),
    path('shimla/hotels/',Hotels_Shimla,name='hotels_shimla'),
    path('manali/',Manali,name='manali'),
    path('manali/hotels/',Hotels_Manali,name='hotels_manali'),
    path('gangtok/',Gangtok,name='gangtok'),
    path('gangtok/hotels/',Hotels_Gangtok,name='hotels_gangtok'),
    path('kerela/',Kerela,name='kerela'),
    path('kerela/hotels/',Hotels_Kerela,name='hotels_kerela'),
    path('kolkata/',Kolkata,name='kolkata'),
    path('kolkata/hotels/',Hotels_Kolkata,name='hotels_kolkata'),
    path('goa/',Goa,name='goa'),
    path('goa/hotels/',Hotels_Goa,name='hotels_goa'),
    path('mumbai/',Mumbai,name='mumbai'),
    path('mumbai/hotels/',Hotels_Mumbai,name='hotels_mumbai'),
]
