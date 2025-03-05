# apps/reservations/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reservation
from apps.chefs.models import Chef
from .serializers import ReservationSerializer
from django.utils import timezone

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    @action(detail=False, methods=['get'], url_path='available')
    def check_availability(self, request):
        chef_id = request.query_params.get('chef_id', None)
        date = request.query_params.get('date', None)
        
        if not chef_id or not date:
            return Response({"error": "chef_id and date are required"}, status=400)

        chef = Chef.objects.get(id=chef_id)
        date = timezone.datetime.strptime(date, "%Y-%m-%d").date()

        is_available = chef.is_available(date)

        return Response({"available": is_available})

    @action(detail=False, methods=['post'], url_path='reserve')
    def reserve_chef(self, request):
        chef_id = request.data.get('chef_id', None)
        date = request.data.get('date', None)
        
        if not chef_id or not date:
            return Response({"error": "chef_id and date are required"}, status=400)

        chef = Chef.objects.get(id=chef_id)
        date = timezone.datetime.strptime(date, "%Y-%m-%d").date()

        if chef.is_available(date):
            reservation = Reservation.objects.create(chef=chef, date=date)
            return Response({"message": "Reservation successful!", "reservation_id": reservation.id}, status=201)
        else:
            return Response({"error": "Chef not available on this date"}, status=400)
