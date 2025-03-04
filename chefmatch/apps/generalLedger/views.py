from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GeneralLedger
from .serializers import GeneralLedgerSerializer

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = GeneralLedger.objects.all()
        serializer = GeneralLedgerSerializer(items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GeneralLedgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = GeneralLedger.objects.get(pk=pk)
    except GeneralLedger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GeneralLedgerSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GeneralLedgerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GeneralLedgerViewSet(viewsets.ModelViewSet):
    queryset = GeneralLedger.objects.all()
    serializer_class = GeneralLedgerSerializer