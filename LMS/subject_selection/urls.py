from django.contrib import admin
from django.urls import path,include
from subject_selection import views

urlpatterns = [
    path('',views.subject_selection,name="subject_selection"),
]