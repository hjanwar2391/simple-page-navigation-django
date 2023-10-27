from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(request):
    return HttpResponse(''' 
                        <h1>this is course page </h1>
                        <a href="/">home</a></br>
                        <a href="/about/">about</a></br>
                        <a href="/contact/">contact</a></br>
                        <a href="/feetback/"> feetback </a>
                        ''')

def feetback(request):
    return HttpResponse('''
                        <h1>this is feetback page</h1>
                        <a href="/">home</a></br>
                        <a href="/about/">about</a></br>
                        <a href="/contact/">contact</a></br>
                        <a href="/course/"> course </a>
                        ''')