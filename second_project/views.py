from django.http import HttpResponse

def home(request):
    return HttpResponse('''
                        <h1>this is a home page</h1>
                        <a href="/about/">about</a></br>
                        <a href="/contact/">contact</a></br>
                        <a href="/feetback/"> feetback </a></br>
                        <a href="/course/"> course </a>
                        ''')