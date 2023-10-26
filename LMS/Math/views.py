from django.shortcuts import render
from django.http import HttpRequest

def unit1(request):
    return render(request,"Math.html")

# Create your views here.
