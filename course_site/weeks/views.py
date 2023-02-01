from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    return TemplateResponse(request,"weeks/home.html",)
    #return (request, 'homeApp/home.html')

def syllabus(request):
    return TemplateResponse(request,"weeks/syllabus.html",)


def class01(request):
     return TemplateResponse( request,"weeks/class01.html",)


def class00(request):
     return TemplateResponse( request,"weeks/class00.html",)

def qm2(request):
     return TemplateResponse( request,"weeks/qm2.html",)
