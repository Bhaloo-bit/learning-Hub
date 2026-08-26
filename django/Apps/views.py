from django.shortcuts import render
from .models import ChaiVarity
# Create your views here.

def books(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'Apps/all_apps.html', {'chais':chais})
