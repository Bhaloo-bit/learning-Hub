from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello world, You at Bhumi Home page")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("hello world, Your at Bhumi About page")  

def contact(request):
    return render(render, "index1.html")