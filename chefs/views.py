from .models import Chef
from rest_framework import viewsets
from .serializers import ChefSerializer

class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
