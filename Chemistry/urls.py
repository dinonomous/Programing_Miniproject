from Chemistry import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('Unit_1',views.unit1,name="scpunit1"),
    path('Unit_2',views.unit2,name="scpunit2"),
    path('Unit_3',views.unit3,name="scpunit3"),
    path('Unit_4',views.unit4,name="scpunit4"),
    path('Unit_5',views.unit5,name="scpunit5"),
]