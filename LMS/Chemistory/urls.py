from django.contrib import admin
from django.urls import path,include
from Chemistory import views

urlpatterns = [
    path('',views.unit1,name="cheunit1"),
]