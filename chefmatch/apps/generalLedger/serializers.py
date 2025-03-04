from .models import GeneralLedger
from rest_framework import serializers

class GeneralLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralLedger
        fields = '__all__'