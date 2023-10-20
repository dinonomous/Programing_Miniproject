from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")


#index.html file is the HTML for landing page file is located in the templates.