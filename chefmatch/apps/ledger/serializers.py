from .models import Ledger
from rest_framework import serializers

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'
