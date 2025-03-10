from datetime import datetime
from .models import Reservation
from rest_framework import serializers

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

def validate(self, data):
        """
        Custom validation to prevent double booking.
        """
        chef = data.get('chef')
        date = data.get('date')

        if chef and date:
            # Check if there is already a reservation for the same chef on the same day
            existing_reservation = Reservation.objects.filter(
                chef=chef,
                date__date=date.date()
            ).exclude(id=self.instance.id if self.instance else None)

            if existing_reservation.exists():
                raise serializers.ValidationError("This chef is already reserved on the selected day.")

        return data