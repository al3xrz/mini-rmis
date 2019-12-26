from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    path('', main_entry_point, name = 'main_entry_point'),


]
