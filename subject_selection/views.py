from django.shortcuts import render
from django.http import HttpResponse

def subject_selection(request):
    return render(request,"subject_selection.html")

# Create your views here.
