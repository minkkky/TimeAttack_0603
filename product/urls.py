from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('drink/', views.make_form,name='drink'),
]