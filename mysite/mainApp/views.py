from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Есть впорос, пиши-звони :', '(101)-102-103', 'examlpe@gmail.com']})