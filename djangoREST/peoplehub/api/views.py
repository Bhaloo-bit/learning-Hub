from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
# Create your views here.

def singleobj(request):
   data = Person.objects.get(id=1)
   serializer = PersonSerializer(data)
   print(serializer.data)
    

def multipleobj(request):
   data = Person.objects.all()
   serializer = PersonSerializer(data, many=True)
   print(serializer)