from django.contrib import admin
from django.urls import path,include
from UnderConstruction import views

urlpatterns = [
    path('',views.unit1,name="underconstruction"),
]