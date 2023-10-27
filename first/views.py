from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse('''
                        <h1>this is about page</h1>
                        <a href="/">home</a>
                        </br>
                        <a href="/contact/">contact</a></br>
                        <a href="/feetback/"> feetback </a></br>
                        <a href="/course/"> course </a>
                        ''')

def contact(request):
    return HttpResponse('''
                        <h1>this is about page</h1>
                        <a href="/">home</a></br>
                        <a href="/about/">about</a></br>
                        <a href="/feetback/"> feetback </a></br>
                        <a href="/course/"> course </a>
                        ''')