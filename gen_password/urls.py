from django.forms import PasswordInput
from django.urls import path

from . import views

urlpatterns = [
    path('',  views.index),
    
] 