"""
This module contains the necessary imports and definitions for creating an API using Django REST framework.

The module imports the necessary modules from Django REST framework, including viewsets, status, decorators, and response.

It also imports the models and serializers from the current app, which are used to interact with the database and serialize data.

The module defines two API views:
- item_list: This view handles GET and POST requests for listing and creating specialties.
- item_detail: This view handles GET, PUT, and DELETE requests for retrieving, updating, and deleting a specific specialty.

The module also defines a ViewSet, SpecialtyViewSet, which uses the ModelViewSet class from Django REST framework to manage specialties.

The queryset for the ViewSet is set to retrieve all specialties from the database.

The serializer_class for the ViewSet is set to use the SpecialtySerializer for serializing specialties.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Specialty
from .serializers import SpecialtySerializer

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Specialty.objects.all()
        serializer = SpecialtySerializer(items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SpecialtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Specialty.objects.get(pk=pk)
    except Specialty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpecialtySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SpecialtySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer