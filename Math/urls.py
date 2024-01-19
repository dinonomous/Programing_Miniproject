from django.contrib import admin
from django.urls import path,include
from Math import views

urlpatterns = [
    path('Unit_1',views.unit1,name="mathunit1"),
]