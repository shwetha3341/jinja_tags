from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d ={'name':'shwetha','age':16}
    return render(request,'h1.html',d)

def jinja_operational(request):
    d = {'a':10,'b':20}
    return render(request,'h2.html',d)    