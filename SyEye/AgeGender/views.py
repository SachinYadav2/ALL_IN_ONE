from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def AG_Home(request):
    return render(request , "AgeGender/home.html")
    
