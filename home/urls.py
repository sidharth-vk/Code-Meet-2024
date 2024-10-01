
from django.urls import path
from .views import *


urlpatterns = [

    path('',home,name="home"),
    path('treasure_hunt',treasure_hunt,name="treasure_hunt"),
    path('geo_guesser',geo_guesser,name="geo_guesser"),
    path('paper_pitch',paper_pitch,name="paper_pitch"),

]
