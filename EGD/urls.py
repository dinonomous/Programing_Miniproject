from django.contrib import admin
from django.urls import path,include
from EGD import views

urlpatterns = [
    path('week1',views.week1,name="EGDweek1"),
    path('week2',views.week2,name="EGDweek1"),
    path('week3',views.week3,name="EGDweek1"),
    path('week4',views.week4,name="EGDweek1"),
    path('week5',views.week5,name="EGDweek1"),
    path('week6',views.week6,name="EGDweek1"),
    path('week7',views.week7,name="EGDweek1"),
    path('week8',views.week8,name="EGDweek1"),
    path('week9',views.week9,name="EGDweek1"),
    path('week10',views.week10,name="EGDweek1"),
    path('week11',views.week11,name="EGDweek1"),
    path('week12',views.week12,name="EGDweek1"),
]