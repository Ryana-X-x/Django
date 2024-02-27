from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request, 'home.html')
    #return HttpResponse("<h1>Hello World!</h1>")

def add(request):
    if request.method == 'POST':
        value1 = int(request.POST.get('value1'))
        value2 = int(request.POST.get('value2'))
        result = value1 + value2
        return render(request,'result.html')
    else:
        return HttpResponse('Method not allowed')