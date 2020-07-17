from django.http import HttpResponse
from django.shortcuts import render



def html_demo(request):
    return render(request,"sample1.html")