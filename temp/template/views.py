from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request, 'home.html')
    #return HttpResponse("<h1>Hello World!</h1>")

def add(request):
    if request.method == 'POST':
        try:
            value1 = int(request.POST.get('number1'))
            value2 = int(request.POST.get('number2'))
        except (TypeError, ValueError):
            # Handle the case where values cannot be converted to integers
            return HttpResponse('Invalid input. Please enter valid numbers.')

        result = value1 + value2
        return render(request, 'result.html', {'result': result})
    else:
        return HttpResponse('Method not allowed')
