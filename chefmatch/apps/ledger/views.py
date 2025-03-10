from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Ledger
from .serializers import LedgerSerializer

@api_view(['GET', 'POST'])
def ledger_list(request):
    if request.method == 'GET':
        item = Ledger.objects.all()
        serializer = LedgerSerializer(item, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LedgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    item = get_object_or_404(Ledger, pk=pk)

    if request.method == 'GET':
        serializer = LedgerSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LedgerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer