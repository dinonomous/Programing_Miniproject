from django.contrib import admin
from django.urls import path,include
from Chemistry import views

urlpatterns = [
    path('',views.unit1,name="cheunit1"),
]