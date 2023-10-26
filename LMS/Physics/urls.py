from django.contrib import admin
from django.urls import path,include
from Physics import views

urlpatterns = [
    path('',views.unit1,name="phyunit1"),
]