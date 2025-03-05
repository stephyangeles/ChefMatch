from .models import Specialty, Reservation
from rest_framework import serializers

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

