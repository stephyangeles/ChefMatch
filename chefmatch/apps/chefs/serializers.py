from .models import Chef
from rest_framework import serializers

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'
