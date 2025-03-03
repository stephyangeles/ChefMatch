from .models import Specialty, Chef
from rest_framework import serializers

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['id', 'name', 'expertise', 'rating']
