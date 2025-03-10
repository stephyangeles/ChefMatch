from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Chef
from .serializers import ChefSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = Chef.objects.all()
        serializer = ChefSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChefSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def chef_detail(request, pk):
    chef = get_object_or_404(Chef, pk=pk)

    if request.method == 'GET':
        serializer = ChefSerializer(chef)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChefSerializer(chef, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chef.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer