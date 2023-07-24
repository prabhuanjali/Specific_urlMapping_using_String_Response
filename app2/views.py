from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('First response of App2')


def second(request):
    return HttpResponse('Second response of App2')