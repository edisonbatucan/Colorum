from cv2 import imread
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SUV
from .serializers import SUVSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class SUVAPIView(APIView):

    def get(self, request):
        suvs = SUV.objects.all()
        serializer = SUVSerializer(suvs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SUVSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SUVDetails(APIView):

    def get_object(self, id):
        try:
            return SUV.objects.get(id=id)
        except SUV.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        suv = self.get_object(id)
        serializer = SUVSerializer(suv)
        return Response(serializer.data)

    def put(self, request, id):
        suv = self.get_object(id)
        serializer = SUVSerializer(suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        suv = self.get_object(id)
        suv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def suv_list(request):
    if request.method == 'GET':
        suvs = SUV.objects.all()
        serializer = SUVSerializer(suvs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SUVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def suv_detail(request, pk):
    try:
        suv = SUV.objects.get(pk=pk)
    except SUV.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SUVSerializer(suv)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SUVSerializer(suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        suv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
