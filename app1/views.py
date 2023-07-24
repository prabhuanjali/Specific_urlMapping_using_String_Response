from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse('First response of App1')

def second(request):
    return HttpResponse('Second response of App1')
