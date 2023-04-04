from django.http import HttpResponse
from django.shortcuts import render
def aboutus(request):
    return HttpResponse('Welcome to wscube tech')

def tutorial(request):
    return render(request, 'pages/tutorial.html', {'navbar': 'tutorial'})

def aboutus(request):
    return render(request,'pages/aboutus.html', {'navbar': 'aboutus'})

def homepage(request):
    data = {
        'title' : 'home new'
    }
    return render(request,'index.html',data)

def tutorial1(request):
    return render(request, 'pages/tutorial1.html')