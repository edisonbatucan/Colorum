from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import PickUp
from .serializers import PickUpSerializer

# Create your views here.

def pickup_list(request):
    if request.method == 'GET':
        pickups = PickUp.objects.all()
        serializer = PickUpSerializer(pickups, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PickUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)